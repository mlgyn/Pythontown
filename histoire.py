from brigand import Brigand
from cowboy import Cowboy
from dame import Dame
from barman import Barman
from sherif import Sherif

def histoire():
    # Création des personnages
    brigand = Brigand("Joe le Terrible", "whisky")
    cowboy = Cowboy("Billy", "lait")
    dame = Dame("Miss Rose", "thé", couleur_robe="bleue")
    barman = Barman("John", "Chez le Pistolero")
    sherif = Sherif("Hank", "eau")

    # Scène 1 : Présentation des personnages
    print("\n--- Le soleil brille sur la ville poussiéreuse de Deadwood Valley ---\n")
    brigand.se_presenter()
    cowboy.se_presenter()
    dame.se_presenter()
    barman.se_presenter()
    sherif.se_presenter()

    # Scène 2 : Joe le Terrible entre dans le saloon
    print("\n--- Joe le Terrible entre dans le saloon, un sourire moqueur sur les lèvres ---\n")
    brigand.parle("Eh bien, eh bien... Ce saloon est un endroit parfait pour moi.")

    brigand.manger()  # Le brigand se sert un repas salissant
    brigand.parle("Donne-moi un verre de whisky, John ! Et prépare-toi, ça va être une longue nuit.")
   
    # Le barman sert à Joe son verre de whisky
    barman.servir(brigand)
    brigand.boire()  # Le brigand boit bruyamment

    # Scène 3 : Le barman observe, le saloon est sous tension
    print("\n--- Le barman John observe Joe avec méfiance, mais reste calme ---\n")
    barman.servir(brigand)  # Il sert un autre verre
    barman.manger()  # Le barman mange en servant le brigand

    # Le brigand kidnappe la dame
    brigand.kidnapper(dame)
    brigand.parle("Tu viens avec moi, Miss Rose, ou je t'emmène de force.")

    # Scène 4 : Le cowboy Billy apprend que Miss Rose a été enlevée
    print("\n--- Billy le Courageux entend les cris de Miss Rose ---\n")
    cowboy.parle("Joe le Terrible a kidnappé Miss Rose ! Pas question de laisser ça passer.")
    sherif.rechercher_brigand(brigand)
    
    # Avant de partir, le barman sert à Billy son verre de lait
    barman.servir(cowboy)
    cowboy.boire()  # Billy boit un verre de lait avant d’agir

    cowboy.manger()  # Billy mange un petit encas pour se préparer à la mission

    # Scène 5 : Le shérif Hank rejoint Billy
    print("\n--- Le shérif Hank, calme et méthodique, rejoint Billy le Courageux ---\n")
    sherif.parle("Je n'aime pas ce genre de situation. Mais la loi, c'est la loi.")
    
    # Le barman sert à Sherif son verre
    barman.servir(sherif)
    sherif.boire()  # Le shérif boit son verre
    sherif.manger()  # Le shérif prend un moment pour un repas rapide avant de partir

    # Scène 6 : Confrontation dans le désert, le cowboy et le brigand se rencontrent
    print("\n--- Billy le Courageux et Joe le Terrible se confrontent dans le désert ---\n")
    cowboy.parle("Joe, tu vas payer pour ce kidnapping !")
    brigand.parle("Ha ! Tu crois pouvoir me stopper, Billy ? Viens me chercher si tu oses.")
    
    cowboy.tirer_sur(brigand)  # Le cowboy tire sur le brigand
    brigand.se_faire_emprisonner(cowboy)  # Le brigand est capturé

    # Scène 7 : Le cowboy libère Miss Rose
    print("\n--- Billy le Courageux et le shérif Hank trouvent Miss Rose attachée ---\n")
    cowboy.liberer(dame)
    dame.parle("Merci, Billy ! Vous êtes un héros. Mais... pouvez-vous m’offrir un verre de thé ?")
    
    # Le barman sert le thé à Miss Rose
    barman.servir(dame)
    dame.boire()  # Miss Rose boit son thé

    # Scène 8 : Miss Rose change de robe pour célébrer sa liberté
    print("\n--- Miss Rose se débarrasse de sa robe captive et s'offre une nouvelle robe ---\n")
    dame.changer_de_robe("verte")
    dame.manger()  # Miss Rose prend un moment pour manger quelque chose de délicieux

    # Scène 9 : Joe le Terrible est ramené au saloon et tout le monde célèbre
    print("\n--- Le shérif et Billy ramènent Joe le Terrible au saloon, tout le monde observe ---\n")
    cowboy.parle("Dry Gulch est de nouveau en sécurité grâce à moi.")
    brigand.parle("Je ne vous oublie pas, Billy. Un jour, je reviendrai.")
    dame.parle("Merci, Billy, vous êtes un véritable héros.")
    sherif.parle("Joe le Terrible est derrière les barreaux grâce à la loi.")
    barman.parle("Un autre jour paisible à Deadwood Valley, Coco.\n")
    
    # Le barman sert à tout le monde un dernier verre
    barman.servir(cowboy)
    barman.servir(sherif)
    barman.servir(dame)
    barman.servir(barman)
    barman.manger()  # Le barman mange tranquillement alors que tout se calme

    print("\n--- Le saloon éclate en applaudissements, et les habitants de Dry Gulch se détendent enfin ---\n")
