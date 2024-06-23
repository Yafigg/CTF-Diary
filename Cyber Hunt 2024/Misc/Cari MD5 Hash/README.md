# Description

Cari md5hash dapet flag e69804589d0fbf65582f1df23a1bb687

# Solution 

Kita diberikan file unzip, langsung saja kita buka hasil dari unzip
```
❯ cd 'cari md5hash'
❯ ls
100.txt  133.txt  166.txt  199.txt  230.txt  263.txt  296.txt  328.txt  360.txt  393.txt  425.txt  458.txt  490.txt  71.txt
101.txt  134.txt  167.txt  19.txt   231.txt  264.txt  297.txt  329.txt  361.txt  394.txt  426.txt  459.txt  491.txt  72.txt
102.txt  135.txt  168.txt  1.txt    232.txt  265.txt  298.txt  32.txt   362.txt  395.txt  427.txt  45.txt   492.txt  73.txt
103.txt  136.txt  169.txt  200.txt  233.txt  266.txt  299.txt  330.txt  363.txt  396.txt  428.txt  460.txt  493.txt  74.txt
104.txt  137.txt  16.txt   201.txt  234.txt  267.txt  29.txt   331.txt  364.txt  397.txt  429.txt  461.txt  494.txt  75.txt
105.txt  138.txt  170.txt  202.txt  235.txt  268.txt  2.txt    332.txt  365.txt  398.txt  42.txt   462.txt  495.txt  76.txt
106.txt  139.txt  171.txt  203.txt  236.txt  269.txt  300.txt  333.txt  366.txt  399.txt  430.txt  463.txt  496.txt  77.txt
107.txt  13.txt   172.txt  204.txt  237.txt  26.txt   301.txt  334.txt  367.txt  39.txt   431.txt  464.txt  497.txt  78.txt
108.txt  140.txt  173.txt  205.txt  238.txt  270.txt  302.txt  335.txt  368.txt  3.txt    432.txt  465.txt  498.txt  79.txt
109.txt  141.txt  174.txt  206.txt  239.txt  271.txt  303.txt  336.txt  369.txt  400.txt  433.txt  466.txt  499.txt  7.txt
10.txt   142.txt  175.txt  207.txt  23.txt   272.txt  304.txt  337.txt  36.txt   401.txt  434.txt  467.txt  49.txt   80.txt
110.txt  143.txt  176.txt  208.txt  240.txt  273.txt  305.txt  338.txt  370.txt  402.txt  435.txt  468.txt  4.txt    81.txt
111.txt  144.txt  177.txt  209.txt  241.txt  274.txt  306.txt  339.txt  371.txt  403.txt  436.txt  469.txt  500.txt  82.txt
112.txt  145.txt  178.txt  20.txt   242.txt  275.txt  307.txt  33.txt   372.txt  404.txt  437.txt  46.txt   50.txt   83.txt
113.txt  146.txt  179.txt  210.txt  243.txt  276.txt  308.txt  340.txt  373.txt  405.txt  438.txt  470.txt  51.txt   84.txt
114.txt  147.txt  17.txt   211.txt  244.txt  277.txt  309.txt  341.txt  374.txt  406.txt  439.txt  471.txt  52.txt   85.txt
115.txt  148.txt  180.txt  212.txt  245.txt  278.txt  30.txt   342.txt  375.txt  407.txt  43.txt   472.txt  53.txt   86.txt
116.txt  149.txt  181.txt  213.txt  246.txt  279.txt  310.txt  343.txt  376.txt  408.txt  440.txt  473.txt  54.txt   87.txt
117.txt  14.txt   182.txt  214.txt  247.txt  27.txt   311.txt  344.txt  377.txt  409.txt  441.txt  474.txt  55.txt   88.txt
118.txt  150.txt  183.txt  215.txt  248.txt  280.txt  312.txt  345.txt  378.txt  40.txt   442.txt  475.txt  56.txt   89.txt
119.txt  151.txt  184.txt  216.txt  249.txt  281.txt  313.txt  346.txt  379.txt  410.txt  443.txt  476.txt  57.txt   8.txt
11.txt   152.txt  185.txt  217.txt  24.txt   282.txt  314.txt  347.txt  37.txt   411.txt  444.txt  477.txt  58.txt   90.txt
120.txt  153.txt  186.txt  218.txt  250.txt  283.txt  315.txt  348.txt  380.txt  412.txt  445.txt  478.txt  59.txt   91.txt
121.txt  154.txt  187.txt  219.txt  251.txt  284.txt  316.txt  349.txt  381.txt  413.txt  446.txt  479.txt  5.txt    92.txt
122.txt  155.txt  188.txt  21.txt   252.txt  285.txt  317.txt  34.txt   382.txt  414.txt  447.txt  47.txt   60.txt   93.txt
123.txt  156.txt  189.txt  220.txt  253.txt  286.txt  318.txt  350.txt  383.txt  415.txt  448.txt  480.txt  61.txt   94.txt
124.txt  157.txt  18.txt   221.txt  254.txt  287.txt  319.txt  351.txt  384.txt  416.txt  449.txt  481.txt  62.txt   95.txt
125.txt  158.txt  190.txt  222.txt  255.txt  288.txt  31.txt   352.txt  385.txt  417.txt  44.txt   482.txt  63.txt   96.txt
126.txt  159.txt  191.txt  223.txt  256.txt  289.txt  320.txt  353.txt  386.txt  418.txt  450.txt  483.txt  64.txt   97.txt
127.txt  15.txt   192.txt  224.txt  257.txt  28.txt   321.txt  354.txt  387.txt  419.txt  451.txt  484.txt  65.txt   98.txt
128.txt  160.txt  193.txt  225.txt  258.txt  290.txt  322.txt  355.txt  388.txt  41.txt   452.txt  485.txt  66.txt   99.txt
129.txt  161.txt  194.txt  226.txt  259.txt  291.txt  323.txt  356.txt  389.txt  420.txt  453.txt  486.txt  67.txt   9.txt
12.txt   162.txt  195.txt  227.txt  25.txt   292.txt  324.txt  357.txt  38.txt   421.txt  454.txt  487.txt  68.txt
130.txt  163.txt  196.txt  228.txt  260.txt  293.txt  325.txt  358.txt  390.txt  422.txt  455.txt  488.txt  69.txt
131.txt  164.txt  197.txt  229.txt  261.txt  294.txt  326.txt  359.txt  391.txt  423.txt  456.txt  489.txt  6.txt
132.txt  165.txt  198.txt  22.txt   262.txt  295.txt  327.txt  35.txt   392.txt  424.txt  457.txt  48.txt   70.txt
```
Njirrlah kita ternyata dikasih file yang banyak gini, tapi tenang saya masih mengingat command untuk bisa membuka 1 persatu file yang berformat .txt dan menampilkannya, berikut command nya
```
❯ find . -type f -exec cat {} +
```
namun outputnya sangat banyak sekali dan saya sudah mencoba dengan mengrep CYHUNT24 tidak ketemu, berarti apa solusinya ? yapp scroll sampai ketemu, ternyata ga jauh dari bawah ku scroll langsung dapat Md5hash_f1le_itu_Koenji, tinggal kita bungkus dengan format flagnya CYHUNT24{Md5hash_f1le_itu_Koenji}

# FLAG : CYHUNT24{Md5hash_f1le_itu_Koenji}
