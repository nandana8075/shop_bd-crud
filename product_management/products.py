from unicodedata import category

import mysql.connector
class ProductManager:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nandana@123",
            database="shop_db"
        )
        print("connection established..!")

    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from product"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for data in records:
                print(data)
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from product where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            return records
        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            record=self.get_object(id=id)
            if record==None:
                print("product not found")
            print(record)
        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query ="insert into product (name,category,price,quantity,manufacturer) values (%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("product details added successfully...!")
        except Exception as e:
            print(e)

    def put (self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s"
                placeholder=placeholder.rstrip(",")
                query=f"update product set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("product details updated successfully..!")
            else:
                print("product not found")
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            if record!=None:
                query="delete from product where id=%s"
                values=(id,)
                self.cursor.execute(query.values)
                self.connection.commit()
                print("product deleted successfully..!")
            else:
                print("product not found..!")
        except Exception as e:
            print(e)










product_instance=ProductManager()
product_instance.get()
product_instance.get_object(2)
product_instance.retrieve(2)
#product_instance.post(name="dairy milk",category="chocolate",price=150,quantity=2,manufacturer="cadbury")
product_instance.put(id=3,price=250.50)
#product_instance.delete(1)