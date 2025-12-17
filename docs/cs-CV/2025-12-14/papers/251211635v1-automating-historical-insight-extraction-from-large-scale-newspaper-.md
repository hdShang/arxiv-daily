---
layout: default
title: Automating Historical Insight Extraction from Large-Scale Newspaper Archives via Neural Topic Modeling
---

# Automating Historical Insight Extraction from Large-Scale Newspaper Archives via Neural Topic Modeling

**arXiv**: [2512.11635v1](https://arxiv.org/abs/2512.11635) | [PDF](https://arxiv.org/pdf/2512.11635.pdf)

**作者**: Keerthana Murugaraj, Salima Lamsiyah, Marten During, Martin Theobald

---

## 💡 一句话要点

**应用BERTopic从大规模历史报纸档案中自动化提取主题，以分析核能话语演变**

**关键词**: `神经主题建模` `历史文本分析` `BERTopic` `核能话语` `主题演变` `大规模档案处理`

## 📋 核心要点

1. 核心问题：传统主题建模方法难以处理历史报纸档案中的主题演变、OCR噪声和大规模文本复杂性
2. 方法要点：采用基于Transformer嵌入的BERTopic进行神经主题建模，以提升主题提取的上下文敏感性和可扩展性
3. 实验或效果：分析1955-2018年核能与核安全相关文章，揭示主题分布、时间演变及核能与核武器主题的共现模式

## 📄 摘要（原文）

> Extracting coherent and human-understandable themes from large collections of unstructured historical newspaper archives presents significant challenges due to topic evolution, Optical Character Recognition (OCR) noise, and the sheer volume of text. Traditional topic-modeling methods, such as Latent Dirichlet Allocation (LDA), often fall short in capturing the complexity and dynamic nature of discourse in historical texts. To address these limitations, we employ BERTopic. This neural topic-modeling approach leverages transformerbased embeddings to extract and classify topics, which, despite its growing popularity, still remains underused in historical research. Our study focuses on articles published between 1955 and 2018, specifically examining discourse on nuclear power and nuclear safety. We analyze various topic distributions across the corpus and trace their temporal evolution to uncover long-term trends and shifts in public discourse. This enables us to more accurately explore patterns in public discourse, including the co-occurrence of themes related to nuclear power and nuclear weapons and their shifts in topic importance over time. Our study demonstrates the scalability and contextual sensitivity of BERTopic as an alternative to traditional approaches, offering richer insights into historical discourses extracted from newspaper archives. These findings contribute to historical, nuclear, and social-science research while reflecting on current limitations and proposing potential directions for future work.

