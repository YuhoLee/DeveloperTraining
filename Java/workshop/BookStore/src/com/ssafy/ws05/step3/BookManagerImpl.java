package com.ssafy.ws05.step3;
import java.util.ArrayList;
import java.util.Arrays;

public class BookManagerImpl implements IBookManager{
    private static BookManagerImpl bmi; 
    private int MAX_SIZE = 100;
    private ArrayList<Book> books;
    private int size = 0;
    
    public static BookManagerImpl getInstance() {
        if(bmi == null) {
            bmi = new BookManagerImpl();
        }
        return bmi;
    }
    
    private BookManagerImpl() {
        books = new ArrayList<>();
    }
    
    public void add(Book book) {
        int idx = indexOf(book.getIsbn());
        if(idx != -1) {
            System.out.println(book.getIsbn() + " / " + book.getTitle() + "<----" + "중복되는 도서번호 삽입 시도!!");
            return;
        }
        else {
            books.add(book);
        }
    }
    
    public void remove(String isbn) {
        int index = indexOf(isbn);
        books.remove(index);
    }
    
    public Book[] getList() {
        Book[] copyBook = books.toArray(new Book[0]);
        return copyBook;
    }
    
    public Book searchByIsbn(String isbn) {
        int index = indexOf(isbn);
        if(index != -1) {
            return books.get(index);
        }
        return null;
    }
    
    public Book[] searchByTitle(String title) { //
        ArrayList<Book> titleBooks = new ArrayList<>();
        for(Book b: books) {
            if(b.getTitle().contains(title)) {
                titleBooks.add(b);
            }
        }
        if(!titleBooks.isEmpty()) {
            return titleBooks.toArray(new Book[0]); 
        }
        else { return null; }
    }
    
    public Book[] getBooks() {  //
        ArrayList<Book> titleBooks = new ArrayList<>();
        for(Book b: books) {
            if(!(b instanceof Magazine)) {
                titleBooks.add(b);
            }
        }
        if(!titleBooks.isEmpty()) {
            return titleBooks.toArray(new Book[0]); 
        }
        else { return null; }
    }
    
    public Magazine[] getMagazine() {   //
        ArrayList<Magazine> titleBooks = new ArrayList<>();
        for(Book b: books) {
            if(b instanceof Magazine) {
                titleBooks.add((Magazine)b);
            }
        }
        if(!titleBooks.isEmpty()) {
            return titleBooks.toArray(new Magazine[0]); 
        }
        else { return null; }
    }
    
    public int getTotalPrice() {
        int total = 0;
        for(Book b: books) {
            total += b.getPrice() * b.getQuantity();
        }
        return total;
    }
    
    public double getPriceAvg() {
        double priceSum = getTotalPrice();
        int cnt = 0;
        for(Book b: books) {
            cnt += b.getQuantity();
        }
        return priceSum / (double)cnt;
    }
    
    public void sell(String isbn, int quantity) throws ISBNNotFoundException, QuantityException{
        Book b = searchByIsbn(isbn);
        if(b == null) {
            throw new ISBNNotFoundException();
        }
        else {
            if(b.getQuantity() < quantity) {
                throw new QuantityException();
            }
            else {
                b.changeQuantity(-1 * quantity);
                System.out.println("(" + b.getIsbn() + ")" + b.getTitle() + "책을 " + quantity + "권 팔았습니다.");
            }
        }
    }
    public void buy(String isbn, int quantity) throws ISBNNotFoundException {
        Book b = searchByIsbn(isbn);
        if(b == null) {
            throw new ISBNNotFoundException();
        }
        else {
            b.changeQuantity(quantity);
            System.out.println("(" + b.getIsbn() + ")" + b.getTitle() + "책을 " + quantity + "권 샀습니다.");
        }
    }

    
    private int indexOf(String isbn) {
        int i = 0;
        for(Book b: books) {
            if(isbn.equals(b.getIsbn())) {
                return i;   // empno의 index
            }
            i += 1;
        }
        return -1;      // 동일한 idex 없음
    }
    
}
