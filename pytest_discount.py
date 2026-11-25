from discount import calcualate_discount 

def test_discount_above_15000():
    discount, final=calculate_discount(20000)
      assert discount == 3000
      assert fianl == 1700

def test_discount_below_15000():
    discount, final=calcualte_discount(10000)
      assert discount == 500
      assert final == 1500

def test_discount_at_15000():
    discount, final=calculate_discount(150000)
      assert discount == 2250
      assert final == 12750
