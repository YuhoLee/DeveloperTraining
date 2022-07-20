package com.java.third;
import java.util.ArrayList;

public interface IProductMgr {
	public void add(Product pd);
	public void remove(String pdNum);
	public ArrayList<Product> getList();
	public Product searchByNum(String num);
	public ArrayList<Product> searchByName(String name);
	public ArrayList<Product> getTV();
	public ArrayList<Product> getRefrigerator();
	public ArrayList<Refrigerator> searchVolumeOver(int volume);
	public ArrayList<TV> searchInchOver(int inch);
	public void modifyPrice(Product pd, int price);
	public void getTotalPrice();
	public void buy(String pdNum, int quantity) throws PdNumNotFoundException;
	public void sell(String pdNum, int quantity) throws PdNumNotFoundException, QuantityException;
	
}
