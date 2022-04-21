# coding: utf8

import datetime
import json
import module.bde
class drive:

    def __init__(self, botconfig, mtypecom, mst, userid, username, fstname, msgtime):
        self.botconfig = botconfig
        self.mtypecom = mtypecom
        self.mst = mst
        self.userid = userid
        self.username = username
        self.fstname = fstname
        self.msgtime = msgtime
        answerlink = botconfig['answer']
        self.answerlink = answerlink
        
        self.bbit = True
        self.text = 'Не понимаю('
        self.btc = 1
        self.btn = ['К меню:']
        self.btcom = ['/menu']
        
        with open(answerlink, encoding="utf-8") as a:
            answer = json.load(a)
            
        self.answer = answer
        
        # Если команда:
        if mtypecom == True:
            
            # Если старт:
            if mst == '/start':
                self.bbit = True
                self.text = fstname + answer['starter']
                self.btc = 1
                self.btn = ['Меню']
                self.btcom = ['/menu']
                
                
                now = datetime.datetime.now()
                logtime = str(now)
                with open ( 'logs.log', 'a', encoding='utf-8') as f:
                    f.write(logtime + ' ' + username + '\n')
            
            # Если меню:
            elif mst == '/menu':
                self.bbit = True
                self.text = answer['mmenu']
                self.btc = 5
                self.btn = ['Help', 'Notes', 'Calendar (UC)', 'Storage(UC)', 'About']
                self.btcom = ['/help', '/notes', '/calendar', '/storage', '/about']
            
            # Если помощь:
            elif mst == '/help':
                self.bbit = True
                self.text = answer['helper']
                self.btc = 1
                self.btn = ['Назад']
                self.btcom = ['/menu']
            
            #  Если о программе:  
            elif mst == '/about':
                self.bbit = True
                self.text = answer['abouter']
                self.btc = 1
                self.btn = ['Назад']
                self.btcom = ['/menu']
            
            # Если записи:
            elif mst == '/notes':
                self.bbit = True
                
                # Есть ли записи в БД?
                records = module.bde.exist(userid)
                
                if records == False:
                    self.text = answer['notes']
                    self.btc = 2
                    self.btn = ['Добавить запись', 'Назад']
                    self.btcom = ['/mknote', '/menu']
                    
                else:
                    self.text = answer['notes']
                    self.btc = 4
                    self.btn = ['Вывести список', 'Добавить', 'Удалить', 'Назад']
                    self.btcom = ['/nlist', '/mknote', '/ndel', '/menu']
                
                module.bde.statusbit(userid, 0)   
                  
            elif mst == '/mknote':
                self.bbit = True
                self.text = answer['nadd'] 
                self.btc = 1
                self.btn = ['Назад']
                self.btcom = ['/notes']
                module.bde.statusbit(userid, 1)
            
            # Вывод динамического списка на открытие:    
            elif mst == '/nlist':
                self.text = 'Список записей:' 
                self.btc = module.bde.count(userid)
                self.btc = int(self.btc[0])
                zlist = module.bde.rnote(userid, 'notename')
                print(self.btn)
                slist = module.bde.rnote(userid, 'notetime')
                
                adslash1 = '/addtonote'
                adslash2 = ''
                                
                self.btcom = module.bde.sqltopy(slist, self.btc, adslash2)
                print(self.btcom)
                
                self.btn = module.bde.sqltopy(zlist, self.btc, adslash2)
                print(self.btn)
                
                i = 0
                while i != self.btc:
                    ibtcom = int(self.btcom[i])
                    value = datetime.datetime.fromtimestamp(ibtcom)
                    vtime = value.strftime('%Y-%m-%d %H:%M:%S')
                    self.btn[i] = vtime + ' ' + self.btn[i]
                    i = i + 1
                
                self.btcom = module.bde.sqltopy(slist, self.btc, adslash1)
                print(self.btcom)
                
                self.btc = self.btc + 1
                                
                self.btn.append('Назад')
                self.btcom.append('/notes')
            
            # Вывод динамического списка на удаление:    
            elif mst == '/ndel':
                self.text = 'Какую запись удалить?:' 
                self.btc = module.bde.count(userid)
                self.btc = int(self.btc[0])
                zlist = module.bde.rnote(userid, 'notename')
                print(self.btn)
                slist = module.bde.rnote(userid, 'notetime')

                
                adslash1 = '/delfromnotes'
                adslash2 = ''
                                
                self.btcom = module.bde.sqltopy(slist, self.btc, adslash2)
                print(self.btcom)
                
                self.btn = module.bde.sqltopy(zlist, self.btc, adslash2)
                print(self.btn)
                
                i = 0
                while i != self.btc:
                    ibtcom = int(self.btcom[i])
                    value = datetime.datetime.fromtimestamp(ibtcom)
                    vtime = value.strftime('%Y-%m-%d %H:%M:%S')
                    self.btn[i] = vtime + ' ' + self.btn[i]
                    i = i + 1
                
                self.btcom = module.bde.sqltopy(slist, self.btc, adslash1)
                print(self.btcom)
                
                self.btc = self.btc + 1
                                
                self.btn.append('Назад')
                self.btcom.append('/notes')
                                
            elif mst == '/storage':
                self.text = answer['plug']
                self.btc = 1
                self.btn = ['Назад']
                self.btcom = ['/menu']
                
            elif mst == '/calendar':
                self.text = answer['plug']
                self.btc = 1
                self.btn = ['Назад']
                self.btcom = ['/menu']
                  
            # Динамические команды и непонимание
            else:
                
                # Команды вывода записей
                if mst.find('/addtonote') != -1:
                    notetime = mst.replace('/addtonote', '')
                    self.text = module.bde.note(notetime)
                    self.btc = 1
                    self.btn = ['Назад']
                    self.btcom = ['/notes']
                
                # Команды удаления записей:
                elif mst.find('/delfromnotes') != -1:
                    notetime = mst.replace('/delfromnotes', '')
                    module.bde.dell(notetime, userid)
                    self.text = 'Успешно удалено'
                    self.btc = 1
                    self.btn = ['Назад']
                    self.btcom = ['/notes']
                        
                else:
                    self.text = 'Не понимаю('
                    self.btc = 1
                    self.btn = ['К меню:']
                    self.btcom = ['/menu']
                      
                
        # Если текст:            
        else:
            print(userid)
            statusbit = module.bde.statusbit(userid, -1)
            
            # Блок проверки и обработки текстовых сообщений
            if statusbit == 1:
                module.bde.wnote(userid, mst, msgtime)
                
                self.text = 'Запись успешно добавлена\n \n' + answer['notes']
                self.btc = 4
                self.btn = ['Вывести список', 'Добавить', 'Удалить', 'Назад']
                self.btcom = ['/nlist', '/mknote', '/ndel', '/menu']
                
                module.bde.statusbit(userid, 0)
                            
    def butbit(self):
        return self.bbit
    
    def butcount(self):
        return self.btc
        
    def butname(self):
        return self.btn

    def butcom(self):
        return self.btcom 
    
    def text(self):
        return self.text
    
    def butmess(self):
        return self.text
        
        