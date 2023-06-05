SELECT Orderlist.date,
COALESCE(SUM(Orderlist.quantity * Medicine.price), 0) AS 销售额,
COALESCE(SUM(Orderlist.quantity * Medicine.price - Orderlist.quantity * Purchase.price), 0) AS 利润
FROM Orderlist
LEFT JOIN Medicine ON Orderlist.m_id = Medicine.id
LEFT JOIN Purchase ON Medicine.id = Purchase.medicine_id AND Purchase.purchase_date = Orderlist.date
WHERE Orderlist.type != "退货" AND Orderlist.is_returned != 1
GROUP BY Orderlist.date;

SELECT Orderlist.date,
       COALESCE(SUM(Purchase.price * Purchase.quantity), 0) AS 成本
FROM Orderlist
         LEFT JOIN Medicine ON Orderlist.m_id = Medicine.id
         LEFT JOIN Purchase ON Medicine.id = Purchase.medicine_id AND Purchase.purchase_date = Orderlist.date
WHERE Purchase.type != "退货" AND Purchase.is_returned != 1
GROUP BY Orderlist.date;

