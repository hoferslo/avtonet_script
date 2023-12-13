import requests
from bs4 import BeautifulSoup
import webbrowser

link = "https://www.avto.net/Ads/results.asp?znamka={znamka}&model={model}&modelID={modelID}&tip={tip}&znamka2={znamka2}&model2={model2}&tip2={tip2}&znamka3={znamka3}&model3={model3}&tip3={tip3}&cenaMin={cenaMin}&cenaMax={cenaMax}&letnikMin={letnikMin}&letnikMax={letnikMax}&bencin={bencin}&starost2={starost2}&oblika={oblika}&ccmMin={ccmMin}&ccmMax={ccmMax}&mocMin={mocMin}&mocMax={mocMax}&kmMin={kmMin}&kmMax={kmMax}&kwMin={kwMin}&kwMax={kwMax}&motortakt={motortakt}&motorvalji={motorvalji}&lokacija={lokacija}&sirina={sirina}&dolzina={dolzina}&dolzinaMIN={dolzinaMIN}&dolzinaMAX={dolzinaMAX}&nosilnostMIN={nosilnostMIN}&nosilnostMAX={nosilnostMAX}&lezisc={lezisc}&presek={presek}&premer={premer}&col={col}&vijakov={vijakov}&EToznaka={EToznaka}&vozilo={vozilo}&airbag={airbag}&barva={barva}&barvaint={barvaint}&doseg={doseg}&EQ1={EQ1}&EQ2={EQ2}&EQ3={EQ3}&EQ4={EQ4}&EQ5={EQ5}&EQ6={EQ6}&EQ7={EQ7}&EQ8={EQ8}&EQ9={EQ9}&KAT={KAT}&PIA={PIA}&PIAzero={PIAzero}&PIAOut={PIAOut}&PSLO={PSLO}&akcija={akcija}&paketgarancije={paketgarancije}&broker={broker}&prikazkategorije={prikazkategorije}&kategorija={kategorija}&ONLvid={ONLvid}&ONLnak={ONLnak}&zaloga={zaloga}&arhiv={arhiv}&presort={presort}&tipsort={tipsort}"


filters = {
    znamka="", 
    model="", 
    modelID="", 
    useDiesel=0,
    tip="", 
    znamka2="", 
    model2="", 
    tip2="",
    znamka3="", 
    model3="", 
    tip3="", 
    cenaMin=100, cenaMax=5000, 
    letnikMin=0, letnikMax=2090, 
    bencin=0, 
    starost2=999, 
    oblika=0, 
    ccmMin=0, ccmMax=99999,
    mocMin=0, mocMax=999999, 
    kmMin=1, kmMax=200000, 
    kwMin=70, kwMax=999,
    motortakt=0, 
    motorvalji=0, 
    lokacija=0, 
    sirina=0, 
    dolzina="", 
    dolzinaMIN=0, dolzinaMAX=100, 
    nosilnostMIN=0, nosilnostMAX=999999, 
    lezisc="", 
    presek=0,
    premer=0, 
    col=0, 
    vijakov=0, 
    EToznaka=0, 
    vozilo="", 
    airbag="", 
    barva="",
    barvaint="", 
    doseg=0, 
    EQ1=1000000000, EQ2=1000000000, EQ3=1000000000, EQ4=100000000, EQ5=1000000000, EQ6=1000000000, EQ7=1110100120, EQ8=101000000, EQ9=1000000020, KAT=1010000000, 
    PIA="", 
    PIAzero="", 
    PIAOut="", 
    PSLO="",
    akcija=0, 
    paketgarancije="", 
    broker=0, 
    prikazkategorije=0, 
    kategorija=0,
    ONLvid=0, 
    ONLnak=0, 
    zaloga=10, 
    arhiv=0, 
    presort=3, 
    tipsort="DESC"
}


# Replace placeholders with actual values
link = link.format(
    filters
)

if filters["useDiesel"]:
    link = link + "&subBENZL=202"


webbrowser.open(link)