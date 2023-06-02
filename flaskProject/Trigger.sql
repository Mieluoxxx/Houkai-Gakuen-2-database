use flask;

CREATE TRIGGER update_stock AFTER INSERT ON Orderlist
FOR EACH ROW
BEGIN
  UPDATE Medicine
  SET stock = stock - NEW.quantity
  WHERE id = NEW.m_id;
END;

CREATE TRIGGER increase_stock AFTER DELETE ON Orderlist
FOR EACH ROW
BEGIN
  UPDATE Medicine
  SET stock = stock + OLD.quantity
  WHERE id = OLD.m_id;
END;

