from fpdf import FPDF

def create_pdf_file(text, name):
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    
    # create a cell
    pdf.multi_cell(0, 10, txt=text)
    
    # save the pdf with name .pdf
    pdf.output(name+".pdf")
    return name+".pdf"

def create_hardskill_retrieval(owner, position, hardskill_rating):
    hr = ""
    for h, r in hardskill_rating:
        hr+= f"{h} dengan rating {r} untuk seberapa baik {owner} miliki,"
    return  f"""
    {owner} memiliki hardskill untuk {position} dengan detail {hr}"""

def create_softskill_retrieval(owner, position, softskill_rating):
    sr = ""
    for s, r in softskill_rating:
        sr+= f"{s} dengan rating {r} untuk seberapa baik {owner} miliki,"
    return  f"""
    {owner} memiliki softskill untuk {position} dengan {sr}"""

def create_keluhan_retrieval(owner, position, keluhan_rating):
    kr = ""
    for k, r in keluhan_rating:
        kr+= f"{k} dengan rating {r} untuk seberapa parah {owner} alami,"
    return  f"""
    {owner} memiliki beberapa keluhan pada posisi {position} yaitu {kr}"""

def create_feedback_prompt(owner, position):
    return f"""
        Berikan umpan balik untuk menjadi {position} yang baik dengan informasi yang {owner} miliki!
        """

def create_learning_path_prompt(owner, position):
    return f"""
        Berikan alur pembelajaran yang baik untuk menjadi {position} yang unggul dan dapat bersaing dengan 
        orang lain dengan informasi {owner} miliki!
        """

def create_skill_gap_prompt(owner, position):
    return f"""
        Beri tahu mengenai skill-skill yang kurang atau tidak dikuasai oleh {owner} baik hardskill maupun softskill 
        untuk menjadi {position} yang baik, tangguh, dan dapat bersaing dengan orang lain berdasarkan informasi 
        atau skill {owner} miliki! 
        """

def create_evaluation_prompt(owner, position):
    return f"""
        Berikan evaluasi atau asesmen ke {owner} mengenai kemampuan atau skill yang dimiliki sebagai {position}
        berdasarkan informasi atau skill {owner} miliki!
    """

def create_content_curation_recommendation_prompt(owner, position):
    return f"""
        Berikan bahan ajar atau konten mengenai {position} yang baik, menantang, dan aktual sesuai dengan 
        perkembangan zaman untuk {owner} berdasarkan informasi atau skill {owner} miliki!
    """

def create_talent_insight_prompt(owner, position):
    return f"""
        Berikan pandangan objektif kepada {owner} mengenai {position} di masa depan dan apa saja yang dibutuhkan 
        {position} di masa depan supaya dapat bersaing dan tangguh di masa depan serta apa yang harus dilakukan 
        {owner} untuk menghadapinya dengan informasi dan skill yang dimiliki oleh {owner}!
    """

def create_development_opportunities_prompt(owner, position):
    return f"""
        Berikan peluang - peluang mengenai perkembangan mengenai {position} baik masa sekarang dan masa depan 
        yang mengikuti perkembangan zaman supaya {owner} dapat menjadi lebih baik dan dapat bersaing di masa 
        depan dan meningkatkan diri serta dapat menjadikan {owner} ahli di {position} dengan menggunakan 
        informasi atau skill yang dimiliki {owner}! 
    """

def create_information_retrieval(owner, position, hardskill, softskill, keluhan):
    hardskill_text = create_hardskill_retrieval(owner, position, hardskill)
    softskill_text = create_softskill_retrieval(owner, position, softskill)
    keluhan_text = create_keluhan_retrieval(owner, position, keluhan)

    return f"{hardskill_text}. {softskill_text}. {keluhan_text}."