---
layout: default
title: Fine-grained Narrative Classification in Biased News Articles
---

# Fine-grained Narrative Classification in Biased News Articles

**arXiv**: [2512.03582v1](https://arxiv.org/abs/2512.03582) | [PDF](https://arxiv.org/pdf/2512.03582.pdf)

**作者**: Zeba Afroz, Harsh Vardhan, Pawan Bhakuni, Aanchal Punia, Rajdeep Kumar, Md. Shad Akhtar

---

## 💡 一句话要点

**提出细粒度叙事分类方法以分析印度新闻媒体中的偏见与宣传**

**关键词**: `细粒度叙事分类` `偏见新闻分析` `宣传数据集` `多跳推理框架` `印度新闻媒体` `意识形态标注`

## 📋 核心要点

1. 核心问题：偏见新闻中的叙事作为宣传认知框架，需细粒度分类以揭示意识形态与传播意图。
2. 方法要点：构建INDI-PROP数据集，含多级标注；开发FANTA和TPTC框架，基于GPT-4o-mini进行多跳推理分类。
3. 实验或效果：评估显示在偏见、叙事和说服技术分类上均显著优于基线方法。

## 📄 摘要（原文）

> Narratives are the cognitive and emotional scaffolds of propaganda. They organize isolated persuasive techniques into coherent stories that justify actions, attribute blame, and evoke identification with ideological camps. In this paper, we propose a novel fine-grained narrative classification in biased news articles. We also explore article-bias classification as the precursor task to narrative classification and fine-grained persuasive technique identification. We develop INDI-PROP, the first ideologically grounded fine-grained narrative dataset with multi-level annotation for analyzing propaganda in Indian news media. Our dataset INDI-PROP comprises 1,266 articles focusing on two polarizing socio-political events in recent times: CAA and the Farmers' protest. Each article is annotated at three hierarchical levels: (i) ideological article-bias (pro-government, pro-opposition, neutral), (ii) event-specific fine-grained narrative frames anchored in ideological polarity and communicative intent, and (iii) persuasive techniques. We propose FANTA and TPTC, two GPT-4o-mini guided multi-hop prompt-based reasoning frameworks for the bias, narrative, and persuasive technique classification. FANTA leverages multi-layered communicative phenomena by integrating information extraction and contextual framing for hierarchical reasoning. On the other hand, TPTC adopts systematic decomposition of persuasive cues via a two-stage approach. Our evaluation suggests substantial improvement over underlying baselines in each case.

