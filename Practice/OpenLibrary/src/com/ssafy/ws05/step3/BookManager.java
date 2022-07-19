package com.ssafy.ws05.step3;
import java.util.Arrays;

public class BookManager {
    private int MAX_SIZE = 100;
    private Book[] books;
    private int size = 0;
    
    public BookManager() {
        books = new Book[100];
    }
    
    public void add(Book book) {
        if(size >= MAX_SIZE) {
            System.out.println("DB 사이즈 초과!!");
            return;
        }
        int idx = indexOf(book.getIsbn());
        if(idx != -1) {
            System.out.println(book.getIsbn() + " / " + book.getTitle() + "<----" + "중복되는 도서번호 삽입 시도!!");
            return;
        }
        books[size] = book;
        size += 1;
    }
    
    public void remove(String isbn) {
        int index = indexOf(isbn);
        books[index] = books[--size];
    }
    
    public Book[] getList() {
        Book[] copyBook = Arrays.copyOf(books, size);
        return copyBook;
    }
    
    public Book searchByIsbn(String isbn) {
        int index = indexOf(isbn);
        if(index != -1) {
            return books[index];
        }
        return null;
    }
    
    public Book[] searchByTitle(String title) { //
        Book[] titleBooks = new Book[100];
        int titleSize = 0;
        for(int i = 0; i < size; i++) {
            if(books[i].getTitle().contains(title)) {
                titleBooks[titleSize] = books[i];
                titleSize += 1;
            }
        }
        Book[] copyBook = Arrays.copyOf(titleBooks, titleSize);
        if(titleSize != 0) { return copyBook; }
        else { return null; }
    }
    
    public Book[] getBooks() {  //
        Book[] titleBooks = new Book[100];
        int titleSize = 0;
        for(int i = 0; i < size; i++) {
            if((books[i] instanceof Book) && (!(books[i] instanceof Magazine))) {
                titleBooks[titleSize] = books[i];
                titleSize += 1;
            }
        }
        Book[] copyBook = Arrays.copyOf(titleBooks, titleSize);
        if(titleSize != 0) { return copyBook; }
        else { return null; }
    }
    
    public Book[] getMagazine() {   //
        Book[] titleBooks = new Book[100];
        int titleSize = 0;
        for(int i = 0; i < size; i++) {
            if(books[i] instanceof Magazine) {
                titleBooks[titleSize] = books[i];
                titleSize += 1;
            }
        }
        Book[] copyBook = Arrays.copyOf(titleBooks, titleSize);
        if(titleSize != 0) { return copyBook; }
        else { return null; }
    }
    
    public int getTotalPrice() {
        int total = 0;
        for(int i = 0; i < size; i++) {
            total += books[i].getPrice();
        }
        return total;
    }
    
    public double getPriceAvg() {
        double priceSum = getTotalPrice();
        return priceSum / (double)size;
    }

    
    private int indexOf(String isbn) {
        for(int i = 0; i < size; i++) {
            if(isbn.equals(books[i].getIsbn())) {
                return i;   // empno의 index
            }
        }
        return -1;      // 동일한 idex 없음
    }
    
}
