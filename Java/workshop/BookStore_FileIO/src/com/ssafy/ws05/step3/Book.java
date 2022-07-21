package com.ssafy.ws05.step3;

import java.io.Serializable;

public class Book implements Serializable{
	private static final long serialVersionUID = 1L;
    private String isbn;
    private String title;
    private String author;
    private String publisher;
    private int price;
    private int quantity;
    private String desc;
    
    public Book() {
        
    }
    
    
    public Book(String isbn, String title, String author, String publisher, int price, int quantity, String desc) {
        super();
        this.isbn = isbn;
        this.title = title;
        this.author = author;
        this.publisher = publisher;
        this.price = price;
        this.quantity = quantity;
        this.desc = desc;
    }


    public String getIsbn() {
        return isbn;
    }


    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }


    public String getTitle() {
        return title;
    }


    public void setTitle(String title) {
        this.title = title;
    }


    public String getAuthor() {
        return author;
    }


    public void setAuthor(String author) {
        this.author = author;
    }


    public String getPublisher() {
        return publisher;
    }


    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }


    public int getPrice() {
        return price;
    }


    public void setPrice(int price) {
        this.price = price;
    }


    public int getQuantity() {
        return quantity;
    }


    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


    public String getDesc() {
        return desc;
    }


    public void setDesc(String desc) {
        this.desc = desc;
    }
    
    public void changeQuantity(int n) {
        this.quantity += n;
    }
    
    @Override
    public String toString() {
        return isbn + "\t | " + title + "\t\t | " + author + "\t | " + publisher + "\t\t | " + price + "  | " + quantity + "\t | " + desc;
    }


}
