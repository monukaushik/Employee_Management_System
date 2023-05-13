from django.urls import path
from . import views

urlpatterns = [
   path('',views.home),
   path('signup/',views.signup,name='signup'),
   path('forgotusername/',views.forgotusername,name='forgotusername'),
   path('forgototp/',views.forgototp,name='forgototp'),
   path('forgotpassword/',views.forgotpassword,name='forgotpassword'),

   path('dep_deshboard/',views.dep_deshboard),
   path('allemployee/',views.allemployee),
   path('update/<int:id>/',views.update),
   path('updatedetails/<int:id>',views.updatedetails,name='updated'),
   path('empleave/',views.empleave,name='empleave'),
   path('empsalary/',views.empsalary,name='empsalary'),
   path('newemp/',views.newemp),
   path('leaveapproval/',views.leaveapproval),
   path('approved1/<int:id>/',views.approved1),

   path('admin_panel/',views.admin_panel),
   path('create_account/',views.create_account),
   path('allemployee2/',views.allemployee2), 
   path('alldepartment/',views.alldepartment,name='alldepartment'),
   path('leave/',views.leave,name='leave'),
   path('salary/',views.salary,name='salary'),

   path('logout/',views.logout,name='logout'),
   path('delete/<int:id>/',views.Delete),
   path('delete1/<int:id>/',views.Delete1),
   path('rejectleave/<int:id>/',views.rejectleave),

   
   path('stdprofile/',views.stdprofile),
   path('stdleave/',views.stdleave,name='stdleave'),
   
]
