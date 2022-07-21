package com.ssafy.ws05.step3;

public interface IBookManager{
    public void add(Book book);
    public void remove(String isbn);
    public Book[] getList();
    public Book searchByIsbn(String isbn);
    public Book[] searchByTitle(String title);
    public Magazine[] getMagazine();
    public Book[] getBooks();
    public int getTotalPrice();
    public double getPriceAvg();
    public void sell(String isbn, int quantity) throws ISBNNotFoundException, QuantityException;
    public void buy(String isbn, int quantity) throws ISBNNotFoundException;
    public void saveData();    
}
