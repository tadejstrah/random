#include<string>
#include<iostream>


using namespace std;

class Vozilo{
    string barva;
    double masa;

    public: Vozilo(string barva, double masa): barva(barva), masa(masa){}   // konstruktor

    virtual void pobarvaj(string b){  //virtual pomeni, da funkcijo v child clasu redefinaš/povoziš. samo če je funkcija virtualna se bo klicala potem funckija od childa in ne od parent classa
        barva = b;
        cout << "barvo vozila sem spremenil na " << b <<"\n";
    };

};


//v c++ vectorju maš lohka sam iste tipe (isto velike). Lohka pa to rešiš da nardiš vector pointerjou na objekte različnih tipov
// std::vector <Vozilo*> vozila;
//vozila.push_back(new Avto(4,1000,"črna"))

class Avto : public Vozilo{
    int st_vrat;
    string barvaKoles;
    public: Avto(int s,double m, string b) : Vozilo(b,m), st_vrat(s){}  //initat morš parent class

    void pobarvaj(string b) override {  //override, ker overrida Vozilo::pobarvaj
        Vozilo::pobarvaj(b);
        barvaKoles = b;
        cout << "barvo koles " << b << "in poklical sem funkcijo pobarvaj na klasu vozilo\n";

    }
};


int main(){

    Avto avto = Avto(4,1000,"črna");
    avto.pobarvaj("bela");

}