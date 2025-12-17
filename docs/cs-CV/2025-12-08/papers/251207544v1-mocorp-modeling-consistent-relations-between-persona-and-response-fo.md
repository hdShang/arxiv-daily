---
layout: default
title: MoCoRP: Modeling Consistent Relations between Persona and Response for Persona-based Dialogue
---

# MoCoRP: Modeling Consistent Relations between Persona and Response for Persona-based Dialogue

**arXiv**: [2512.07544v1](https://arxiv.org/abs/2512.07544) | [PDF](https://arxiv.org/pdf/2512.07544.pdf)

**作者**: Kyungro Lee, Dongha Choi, Hyunju Lee

---

## 💡 一句话要点

**提出MoCoRP框架，通过显式建模人设与回复关系，提升基于人设对话的连贯性。**

**关键词**: `基于人设对话` `NLI关系建模` `对话一致性` `语言模型对齐` `对话生成`

## 📋 核心要点

1. 核心问题：现有基于人设的对话数据集缺乏人设句子与回复间的显式关系，影响模型捕捉人设信息。
2. 方法要点：利用NLI专家提取人设与回复的NLI关系，并集成到语言模型中，支持BART和LLMs的扩展。
3. 实验或效果：在ConvAI2和MPChat数据集上优于基线，提升人设一致性和对话生成质量。

## 📄 摘要（原文）

> As dialogue systems become increasingly important across various domains, a key challenge in persona-based dialogue is generating engaging and context-specific interactions while ensuring the model acts with a coherent personality. However, existing persona-based dialogue datasets lack explicit relations between persona sentences and responses, which makes it difficult for models to effectively capture persona information. To address these issues, we propose MoCoRP (Modeling Consistent Relations between Persona and Response), a framework that incorporates explicit relations into language models. MoCoRP leverages an NLI expert to explicitly extract the NLI relations between persona sentences and responses, enabling the model to effectively incorporate appropriate persona information from the context into its responses. We applied this framework to pre-trained models like BART and further extended it to modern large language models (LLMs) through alignment tuning. Experimental results on the public datasets ConvAI2 and MPChat demonstrate that MoCoRP outperforms existing baselines, achieving superior persona consistency and engaging, context-aware dialogue generation. Furthermore, our model not only excels in quantitative metrics but also shows significant improvements in qualitative aspects. These results highlight the effectiveness of explicitly modeling persona-response relations in persona-based dialogue. The source codes of MoCoRP are available at https://github.com/DMCB-GIST/MoCoRP.

