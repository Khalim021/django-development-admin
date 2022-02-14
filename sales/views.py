import pandas as pd
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .utils import get_customer_from_id, get_sales_man_from_id
# Create your views here.
from sales.models import Sales
from .forms import SalesSearchFrom


def home_view(request):
    df1 = None
    positions_df = None
    # chart = None
    form = SalesSearchFrom(request.POST or None)
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        # print(date_from, date_to, chart_type)

        qs = Sales.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(qs) > 0:
            df1 = pd.DataFrame(qs.values())
            df1['customer_id'] = df1['customer_id'].apply(get_customer_from_id)
            df1['sales_man_id'] = df1['sales_man_id'].apply(get_sales_man_from_id)
            positions_data = []
            for sale in qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'price': pos.price,
                        'quantity': pos.quantity,
                        'sales_id': pos.get_sales_id(),
                    }
                    positions_data.append(obj)
            positions_df = pd.DataFrame(positions_data)

            # chart = get_chart(chart_type, df1)

            df1 = df1.to_html()
            print(df1)
        else:
            print('no value')
    context = {
        'form': form,
        'df1': df1,
        'positions_df': positions_df
    }

    return render(request, 'hello_world.html', context)


class HomeListView(LoginRequiredMixin, ListView):
    model = Sales
    template_name = 'home_list.html'


class SaleDetailView(LoginRequiredMixin, DetailView):
    model = Sales
    template_name = 'detail.html'
