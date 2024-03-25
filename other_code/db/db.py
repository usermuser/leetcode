from your_app.models import Borrower, Loan

# Находим количество заемщиков с закрытыми займами
num_borrowers_with_closed_loans = Borrower.objects.filter(loans__status=2).distinct().count()

print("Число заемщиков с закрытыми займами:", num_borrowers_with_closed_loans)




#####

SELECT COUNT(DISTINCT borrower_id) AS num_borrowers_with_closed_loans
FROM db_loan
WHERE status = 2;
