# Divide et Impera

## Traccia
Si consideri il seguente problema computazionale:
#### input:
Un insieme di punti del piano $\{ p_1 = (x_1, y_1), p_2 = (x2, y2), . . . , p_n = (x_n, y_n) \} \subseteq \mathbb{R}^2$
#### output:
La coppia (una coppia, se ce n’è più di una) a distanza minima.
Ossia, una coppia di punti distinti $p_i, p_j$ , tali che
$$
d(p_i, p_j) = \min{ \{ d(p_h, p_k) : h, k = 1, . . . , n, h \neq k \} }
$$
dove
$$
d(p_i, p_j ) = \sqrt{ (x_i − x_j )^2 + (y_i − y_j)^2 }
$$
è la *distanza Euclidea* fra i due punti.
1. Osservare che esiste un algoritmo ovvio che ha running time O(n^2)
2. Usando la tecnica Divide et Impera, progettare un algoritmo con running time o(n^2).

## Soluzione banale
Confrontare tutte le coppie di punti.
Running time $O(n^2)$.

## Soluzione 1 - non efficiente 
Una prima idea è qualla di *partizionare* i punti di due sottoinsiemi, uno *"destro"* e uno *"sinistro"*.
Per fare ciò, dobbiamo prima ordinare i punti in ordine **non decrescente** secondo l'asse $x$.
Dopodiché poniamo $n/2$ nodi in ciascuna delle due partizioni.

Fatto ciò, possiamo **_ricorsivamente_** ricercare la coppia a distanza minima su entrambi i lati.
Una volta trovate le due coppie su entrambe le partizioni, potremmo scegliere quella minima tra le due coppie trovate.

In realtà questo metodo non è del tutto corretto, in quanto nulla vieta che la coppia a distanza minima sia *"a cavallo"* tra le due partizioni.
Perciò per la ricerca del minimo è necessario considerare tutte le coppie di nodi che hanno estremi in versanti differenti.

Percò, per trovare la coppia a distanza minima, bisogna anche considerare le restanti $n/2 * n/2 \in \Theta(n^2)$ coppie di nodi a cavallo tra le due partizioni.
Perciò asintoticamente questo algoritmo non è megliore del di quello banale!

## Solizione 2 - efficiente
Partiamo dalla seguente osservazione:

Sia $min_L$ e $min_R$ la distanza minima trovata ricorsivamente nelle due partizioni $L$ ed $R$, rispettivamente.
Sia $r = \min{(min_L, min_R)}$.
Allora certamente qualsiasi coppia di nodi $p_i,p_j$ appartenenti ad uno stesso versante, saranno a distanza $d(i,j) >= r$.

Perciò se la coppia di nodi a distanza minima si trova a cavallo tra le due partizioni, certamente essi saranno ad una distanza $<=r$.
Quindi ci basta ridurre l'area di ricerca a tutti quei punti nell'*intorno* $+- r$ dalla metà dell'area.

Ovvero, sia $p_k$ l'ultimo punto più a destra del versante sinistro $L$, con coordinate $x_k, y_k$.


