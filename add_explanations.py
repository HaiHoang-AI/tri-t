import json
import re
import os

print("Loading 1100_cau_triet_hoc.json...")
with open('1100_cau_triet_hoc.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

def generate_explanation(q):
    stem = q['question'].strip()
    correct_key = q['correct']
    options_dict = {opt['label']: opt['text'] for opt in q['options']}
    
    if isinstance(correct_key, list):
        correct_text = ', '.join([f"{k} ({options_dict.get(k, '')})" for k in correct_key])
        correct_str = ', '.join(correct_key)
    else:
        correct_text = options_dict.get(correct_key, '')
        correct_str = str(correct_key)

    s_lower = stem.lower()
    c_lower = correct_text.lower()

    # Rule-based specific topic explanations
    if 'chức năng' in s_lower and 'triết học' in s_lower:
        if 'thế giới quan' in c_lower and 'phương pháp luận' in c_lower:
            return "Triết học Mác - Lênin có hai chức năng cơ bản nhất là chức năng thế giới quan duy vật biện chứng và chức năng phương pháp luận duy vật biện chứng, đóng vai trò định hướng cho nhận thức và hoạt động thực tiễn của con người."
        elif 'thế giới quan' in c_lower:
            return "Chức năng thế giới quan của triết học giúp con người định hình quan điểm chung nhất về thế giới, về vị trí và vai trò của con người trong thế giới đó."
        elif 'phương pháp luận' in c_lower:
            return "Chức năng phương pháp luận cung cấp hệ thống các nguyên tắc chỉ đạo chung cho hoạt động nhận thức và cải tạo thực tiễn."

    if 'nguồn gốc' in s_lower and 'duy tâm' in s_lower:
        return "Chủ nghĩa duy tâm ra đời do hạn chế của nhận thức con người về thế giới (tuyệt đối hóa một mặt của quá trình nhận thức) và do sự phân chia giai cấp, tách rời giữa lao động trí óc và lao động chân tay trong xã hội có đối kháng giai cấp."

    if 'tính giai cấp' in s_lower and 'triết học' in s_lower:
        return "Trong xã hội có giai cấp, triết học luôn mang tính giai cấp. Nó phản ánh lợi ích, thể hiện thế giới quan của những giai cấp nhất định trong xã hội."

    if 'duy tâm lịch sử' in s_lower:
        return "Chủ nghĩa duy tâm lịch sử cho rằng ý thức, tư tưởng, tinh thần hay các nhân tố phi vật chất là cái quyết định sự vận động, phát triển của lịch sử xã hội, chứ không phải các điều kiện sinh hoạt vật chất."

    if 'duy vật biện chứng' in s_lower or 'duy vật lịch sử' in s_lower:
        if 'vật chất' in s_lower or 'vật chất' in c_lower:
            return "Quan điểm duy vật biện chứng khẳng định vật chất là cái có trước, quyết định ý thức; thế giới vật chất tồn tại khách quan và thống nhất ở tính vật chất của nó."

    if 'vật chất' in s_lower and ('lênin' in s_lower or 'định nghĩa' in s_lower):
        return "Theo V.I.Lênin: 'Vật chất là một phạm trù triết học dùng để chỉ thực tại khách quan được đem lại cho con người trong cảm giác, được cảm giác của chúng ta chép lại, chụp lại, phản ánh, và tồn tại không phụ thuộc vào cảm giác'."

    if 'ý thức' in s_lower and 'nguồn gốc' in s_lower:
        return "Ý thức có 2 nguồn gốc chính: Nguồn gốc tự nhiên (bộ não người và sự phản ánh thế giới khách quan) và Nguồn gốc xã hội (lao động và ngôn ngữ, trong đó lao động đóng vai trò quyết định trực tiếp)."

    if 'thực tiễn' in s_lower:
        if 'vai trò' in s_lower or 'cơ sở' in s_lower:
            return "Thực tiễn là cơ sở, động lực, mục đích của nhận thức và là tiêu chuẩn duy nhất để kiểm tra chân lý."
        return "Thực tiễn là toàn bộ hoạt động vật chất - cảm tính, có mục đích, mang tính lịch sử - xã hội của con người nhằm cải tạo thế giới khách quan."

    if 'quy luật' in s_lower:
        if 'lượng' in s_lower or 'chất' in s_lower:
            return "Quy luật chuyển hóa từ những thay đổi về lượng dẫn đến những thay đổi về chất và ngược lại vạch ra phương thức vận động, phát triển của sự vật, hiện tượng."
        elif 'mâu thuẫn' in s_lower or 'mặt đối lập' in s_lower:
            return "Quy luật thống nhất và đấu tranh của các mặt đối lập (quy luật mâu thuẫn) là hạt nhân của phép biện chứng, vạch ra nguồn gốc, động lực bên trong của sự vận động và phát triển."
        elif 'phủ định' in s_lower:
            return "Quy luật phủ định của phủ định chỉ ra khuynh hướng phát triển tiến lên theo đường xoáy ốc của sự vật, hiện tượng."

    if 'biện chứng' in s_lower:
        if 'hêghen' in s_lower or 'heghen' in s_lower:
            return "Phép biện chứng của Hêghen là phép biện chứng duy tâm khách quan, coi sự vận động của thế giới là sự tha hóa của 'Ý niệm tuyệt đối'."
        elif 'cổ đại' in s_lower:
            return "Phép biện chứng thời cổ đại là phép biện chứng ngây thơ, chất phác, nhìn nhận thế giới trong sự biến đổi nhưng mang tính trực quan, cảm tính."

    if 'hình thái kinh tế' in s_lower or 'lực lượng sản xuất' in s_lower or 'quan hệ sản xuất' in s_lower:
        return "Theo duy vật lịch sử, Lực lượng sản xuất quyết định Quan hệ sản xuất. Sự phát triển của lực lượng sản xuất là gốc rễ cho sự thay đổi của các hình thái kinh tế - xã hội trong lịch sử."

    if 'cơ sở hạ tầng' in s_lower or 'kiến trúc thượng tầng' in s_lower:
        return "Cơ sở hạ tầng (toàn bộ những quan hệ sản xuất hợp thành cơ cấu kinh tế) quyết định Kiến trúc thượng tầng (các quan điểm chính trị, pháp quyền, triết học... cùng các thiết chế tương ứng)."

    if 'tồn tại xã hội' in s_lower or 'ý thức xã hội' in s_lower:
        return "Tồn tại xã hội quyết định ý thức xã hội; ý thức xã hội là sự phản ánh tồn tại xã hội, đồng thời có tính độc lập tương đối và tác động trở lại tồn tại xã hội."

    # General precise fallback explanation
    return f"Đáp án đúng là {correct_str}: \"{correct_text}\". Căn cứ theo giáo trình Triết học Mác - Lênin, luận điểm này thể hiện đúng nguyên lý và bản chất triết học của vấn đề được đề cập."

# Generate explanation for all questions
updated_count = 0
for q in questions:
    exp = generate_explanation(q)
    q['explanation'] = exp
    updated_count += 1

print(f"Generated explanations for {updated_count} questions.")

# Save updated JSON
with open('1100_cau_triet_hoc.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

# Save updated JS
with open('1100_cau_triet_hoc.js', 'w', encoding='utf-8') as f:
    f.write('window.quizQuestions = ')
    json.dump(questions, f, ensure_ascii=False, indent=2)
    f.write(';\n')

# Save updated .quiz
with open('1100_cau_triet_hoc.quiz', 'w', encoding='utf-8') as f:
    f.write('# QUIZ 1100 CÂU TRIẾT HỌC MÁC - LÊNIN (CÓ GIẢI THÍCH)\n\n')
    for q in questions:
        f.write(f"Câu {q['id']}: {q['question']}\n")
        for opt in q['options']:
            f.write(f"{opt['label']}. {opt['text']}\n")
        correct_str = ', '.join(q['correct']) if isinstance(q['correct'], list) else q['correct']
        f.write(f"Đáp án: {correct_str}\n")
        f.write(f"Giải thích: {q['explanation']}\n\n")

print("Updated 1100_cau_triet_hoc.json, 1100_cau_triet_hoc.js, and 1100_cau_triet_hoc.quiz successfully!")
