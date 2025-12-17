---
layout: default
title: ContextualSHAP : Enhancing SHAP Explanations Through Contextual Language Generation
---

# ContextualSHAP : Enhancing SHAP Explanations Through Contextual Language Generation

**arXiv**: [2512.07178v1](https://arxiv.org/abs/2512.07178) | [PDF](https://arxiv.org/pdf/2512.07178.pdf)

**作者**: Latifa Dwiyanti, Sergio Ryan Wibisono, Hidetaka Nambo

---

## 💡 一句话要点

**提出ContextualSHAP包，通过集成GPT生成上下文文本解释，以增强SHAP在非技术用户中的可理解性。**

**关键词**: `可解释人工智能` `SHAP解释` `大语言模型集成` `上下文生成` `用户评估` `医疗应用`

## 📋 核心要点

1. SHAP解释缺乏对非技术用户的上下文意义，导致理解困难。
2. 方法结合SHAP与GPT，基于用户参数生成定制化文本解释。
3. 在医疗案例中，用户评估显示生成解释比纯视觉输出更易理解和合适。

## 📄 摘要（原文）

> Explainable Artificial Intelligence (XAI) has become an increasingly important area of research, particularly as machine learning models are deployed in high-stakes domains. Among various XAI approaches, SHAP (SHapley Additive exPlanations) has gained prominence due to its ability to provide both global and local explanations across different machine learning models. While SHAP effectively visualizes feature importance, it often lacks contextual explanations that are meaningful for end-users, especially those without technical backgrounds. To address this gap, we propose a Python package that extends SHAP by integrating it with a large language model (LLM), specifically OpenAI's GPT, to generate contextualized textual explanations. This integration is guided by user-defined parameters (such as feature aliases, descriptions, and additional background) to tailor the explanation to both the model context and the user perspective. We hypothesize that this enhancement can improve the perceived understandability of SHAP explanations. To evaluate the effectiveness of the proposed package, we applied it in a healthcare-related case study and conducted user evaluations involving real end-users. The results, based on Likert-scale surveys and follow-up interviews, indicate that the generated explanations were perceived as more understandable and contextually appropriate compared to visual-only outputs. While the findings are preliminary, they suggest that combining visualization with contextualized text may support more user-friendly and trustworthy model explanations.

