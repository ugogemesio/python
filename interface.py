import sistemadeUsabilidade as tela
import trataAudio
import bancoDeDados

print("Programa para ligar automaticamente para ramais via WeBex")


bancoDeDados.abre_tabela()

bancoDeDados.fornece_ramais()

tela.abre_webex()

tela.maximiza_webex()

tela.vai_para_area_telefone()
tela.cola_ramal()

bancoDeDados.salvaAnalise(trataAudio.analisa_situacao_ramal())
