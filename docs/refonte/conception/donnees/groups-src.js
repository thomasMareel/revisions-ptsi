  const CHAP_GROUPS = [
    // ---- PHYSIQUE ----
    ['ondes',  'Ondes & signaux',   ['regimecontinu','premierordre','rlc','signaux','filtres','ali','oscelec','signum','ondes','optgeo','optique','optiqued','interf','dispinterf']],
    ['meca',   'Mécanique',         ['cinept','mecpt','energie','oscill','mcinc','chcentral','mvtsolide']],
    ['thermo', 'Thermodynamique',   ['thermo1','thermo2','thermo3','machines','changement','diffth','fluides','fluiddyn','ecoulement','ecoulreel','thermoouv']],
    ['emag',   'Électromagnétisme', ['estat','estat2a','emag','induction','maxwell','oemvide','oemcond','lorentz']],
    ['chimie', 'Chimie',            ['atome','molecules','cristallin','cinetique','equilchim','acidobase','precipitation','oxred','eph']],
    ['ref',    'Référence',         ['constantes']],
    // ---- MATHS (à plat) ----
    [null, 'Logique',          ['logique']],
    [null, 'Algèbre',          ['complexes','polynomes']],
    [null, 'Analyse',          ['fonctions','suites','suites2a','contderiv','dl','asympt','primitives','integrales','integ2a','edo','edo2a','series','series2a','fxvect','intgene','serient','intparam','fpv']],
    [null, 'Algèbre linéaire', ['matrices','matrices2a','det','det2a','ev','ev2a','applin','applin2a','projsym','elempropres','reduction','prehilb','isometries']],
    [null, 'Géométrie',        ['geometrie','coniques','conred','courbes','geoplane','geo3d','surfaces']],
    [null, 'Probabilités',     ['denombrmt','proba','va','tribus','espproba','vadisc1','vadisc2']],
    // ---- SI ----
    ['analyse',  'Analyse système', ['ingsys','multiphy']],
    ['meca',     'Mécanique',       ['cine','statique','chaines','transm','conception','dynsolide','dyn2a','energsi','rdm']],
    ['auto',     'Automatique',     ['schblocs','sys1','sys2','stabilite','precision','correcteurs','slci','sysnum']],
    ['elec',     'Électrotechnique',['mcc','cvs','hacheurs','triphase','machalt']],
    ['capteurs', 'Capteurs',        ['capteurs']],
    ['ia',       'Intelligence artificielle', ['ia']],
    ['fab',      'Fabrication',     ['cotation','moulage','deform','usinage','assemblage','addfab','trtherm','trsurf','cnd','ppm']],
    // ---- INFO ----
    ['prog', 'Programmation', ['pybases','pyrepr','pyctrl','pyfonc','pytypes','pytri','pyrec','pynum']],
    // ---- ANGLAIS ----
    ['colle', 'Colle / Oral', ['enusuels','endoc','enavis','enconnect','enreac']],
    ['envoc', 'Vocabulaire thématique', ['envoceco','envocpol','envocsci','envocmed']],
    ['engram', 'Grammaire & traduction', ['engramfa','engramtps','engrammod','engramphr']],
    ['enciv', 'Civilisation', ['encivuk','encivus','encivhist']],
    ['enidi', 'Idiomes & expressions', ['enidiom','enidicol']]
  ];
  // Chapitres de 2ᵉ année (badge « 2ᵉ année » du bandeau de titre, filtre d'année du tiroir)
  window.__YEAR2A = new Set(['serient','fxvect','intgene','intparam','fpv',
    'projsym','elempropres','reduction','prehilb','isometries',
    'tribus','espproba','vadisc1','vadisc2',
    'coniques','courbes','geoplane','geo3d',
    'integ2a','suites2a','series2a','edo2a','ev2a','applin2a','matrices2a','det2a',
    // PT spé (2ᵉ année)
    'conred','surfaces',
    'estat2a','maxwell','oemvide','oemcond','interf','dispinterf','ecoulement','ecoulreel','diffth','thermoouv','ali','oscelec','signum',
    'chaines','dyn2a','correcteurs','multiphy','sysnum','ia','rdm','triphase','machalt','conception','ppm']);
  // Année d'un chapitre (même règle que le tiroir) : 0 = les deux années (anglais,
