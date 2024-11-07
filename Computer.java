public class Computer {
    private double prezzo;
    private double peso;
    private double larghezza;
    private double altezza;
    private double profondita;
    private String produttore;
    private int annoDiProduzione;
    private static int count = 0;

    // Constructor
    public Computer(double prezzo, double peso, double larghezza, double altezza, double profondita,
                     String produttore, int annoDiProduzione) {
        this.prezzo = prezzo;
        this.peso = peso;
        this.larghezza = larghezza;
        this.altezza = altezza;
        this.profondita = profondita;
        this.produttore = produttore;
        this.annoDiProduzione = annoDiProduzione;
        count++;
    }

    // Getters and Setters
    public double getPrezzo() {
        return prezzo;
    }

    public void setPrezzo(double prezzo) {
        this.prezzo = prezzo;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getLarghezza() {
        return larghezza;
    }

    public void setLarghezza(double larghezza) {
        this.larghezza = larghezza;
    }

    public double getAltezza() {
        return altezza;
    }

    public void setAltezza(double altezza) {
        this.altezza = altezza;
    }

    public double getProfondita() {
        return profondita;
    }

    public void setProfondita(double profondita) {
        this.profondita = profondita;
    }

    public String getProduttore() {
        return produttore;
    }

    public void setProduttore(String produttore) {
        this.produttore = produttore;
    }

    public int getAnnoDiProduzione() {
        return annoDiProduzione;
    }

    public void setAnnoDiProduzione(int annoDiProduzione) {
        this.annoDiProduzione = annoDiProduzione;
    }

    // Method to print the number of Computer objects created
    public static int getCount() {
        return count;
    }

    @Override
    public String toString() {
        return "Computer [prezzo=" + prezzo + ", peso=" + peso + ", larghezza=" + larghezza + ", altezza=" + altezza
                + ", profondita=" + profondita + ", produttore=" + produttore + ", annoDiProduzione=" + annoDiProduzione
                + "]";
    }

    public static void main(String[] args) {
        // Create Computer objects
        Computer comp1 = new Computer(1000.0, 2.5, 35.0, 25.0, 2.0, "Dell", 2021);
        Computer comp2 = new Computer(1500.0, 2.0, 30.0, 20.0, 1.5, "HP", 2022);

        // Print the Computer objects
        System.out.println(comp1);
        System.out.println(comp2);

        // Print the number of Computer objects created
        System.out.println("Number of Computer objects created: " + Computer.getCount());
    }
}