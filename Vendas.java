public class Vendas {
    public static void main(String[] args) {
        TicketMachine tm01 = new TicketMachine(50);
        TicketMachine tm02 = new TicketMachine(100);

        tm01.insertMoney(60);
        tm01.getPrice();
        tm01.getBalance();

        tm02.insertMoney(200);
        tm02.getPrice();
        tm02.getBalance();

        System.out.print("Balance"+tm01.getBalance());
        System.out. print("Prince"+tm01.getPrice());

        System.out.print("Balance"+tm02.getBalance());
        System.out. print("Prince"+tm02.getPrice());


        tm01.printTicket();
        tm01.printTotal();
        tm02.printTicket();
        tm02.printTotal();

        tm02.insertMoney(10);
    }
}
