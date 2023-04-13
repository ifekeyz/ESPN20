from django.urls import path
from .import views


urlpatterns = [
    path('', views.login, name='login'),
    path('espn20<str:ref_code>', views.indexref, name='indexref'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('forgotPassword', views.forgotPassword, name='forgotPassword'),
    path('changePassword/<token>',views.changePassword, name="changePassword"),
    path('market_place', views.market_place, name='market_place'),
    path('match_result', views.match_result, name='match_result'),
    path('league', views.league, name='league'),
    path('prediction', views.prediction, name='prediction'),
    path('predict', views.predict, name='predict'),
    path('predict/<int:key_id>', views.singlepredict, name='singlepredict'),
    path('singlegame', views.singlegame, name='singlegame'),
    path('betting', views.betting, name='betting'),
    path('recharge', views.recharge, name='recharge'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('refferal', views.refferal, name='refferal'),
    path('transaction', views.transaction, name='transaction'),
    path('withdrawal', views.withdrawal, name='withdrawal'),
    path('betting_history', views.betting_history, name='betting_history'),
    path('singleleague/<int:single_id>', views.single_league, name='single_league'),
    path('sample', views.sample, name='sample'),
]
