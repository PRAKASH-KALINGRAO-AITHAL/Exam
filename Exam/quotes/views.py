from django.shortcuts import render
from StockTickers.models import Student
def home(request):
    stud=Student.objects.all()
    return render(request,'home.html',{'stud':stud})
def about(request):
    try:
        r=request.GET['r']
        stud = Student.objects.get(RegNum=r)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    return render(request, 'about.html', {'stud': stud})
def optimal(request):
    return render(request,'optimal.html',{})
def stockticks(request):
    import json
    import pandas as pd
    ret_val=gbm()
    json_records = ret_val.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request,'stockticks.html',context)
def gbm(n_years = 1, n_scenarios=10, mu=0.07, sigma=0.15, steps_per_year=252*7*60, s_0=100.0, prices=True):
    """
    Evolution of Geometric Brownian Motion trajectories, such as for Stock Prices through Monte Carlo
    :param n_years:  The number of years to generate data for
    :param n_paths: The number of scenarios/trajectories
    :param mu: Annualized Drift, e.g. Market Return
    :param sigma: Annualized Volatility
    :param steps_per_year: granularity of the simulation
    :param s_0: initial value
    :return: a numpy array of n_paths columns and n_years*steps_per_year rows
    """
    # Derive per-step Model Parameters from User Specifications
    import numpy as np
    import pandas as pd
    dt = 1/steps_per_year
    n_steps = int(n_years*steps_per_year) + 1
    # the standard way ...
    # rets_plus_1 = np.random.normal(loc=mu*dt+1, scale=sigma*np.sqrt(dt), size=(n_steps, n_scenarios))
    # without discretization error ...
    rets_plus_1 = np.random.normal(loc=(1+mu)**dt, scale=(sigma*np.sqrt(dt)), size=(n_steps, n_scenarios))
    rets_plus_1[0] = 1
    ret_val = s_0*pd.DataFrame(rets_plus_1).cumprod() if prices else rets_plus_1-1
    return ret_val

