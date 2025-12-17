---
layout: default
title: UW-BioNLP at ChemoTimelines 2025: Thinking, Fine-Tuning, and Dictionary-Enhanced LLM Systems for Chemotherapy Timeline Extraction
---

# UW-BioNLP at ChemoTimelines 2025: Thinking, Fine-Tuning, and Dictionary-Enhanced LLM Systems for Chemotherapy Timeline Extraction

**arXiv**: [2512.04518v1](https://arxiv.org/abs/2512.04518) | [PDF](https://arxiv.org/pdf/2512.04518.pdf)

**作者**: Tianmai M. Zhang, Zhaoyi Sun, Sihang Zeng, Chenxi Li, Neil F. Abernethy, Barbara D. Lam, Fei Xia, Meliha Yetisgen

---

## 💡 一句话要点

**提出思维链、微调与词典增强的LLM系统，用于从临床笔记中提取化疗时间线**

**关键词**: `化疗时间线提取` `大型语言模型微调` `临床笔记处理` `事件归一化` `思维链推理` `词典增强`

## 📋 核心要点

1. 核心问题：从癌症患者电子健康记录中构建化疗时间线，聚焦于从原始临床笔记生成患者级时间线。
2. 方法要点：采用两步工作流，先由LLM提取化疗事件，再通过算法归一化和聚合事件；评估思维链、监督微调、直接偏好优化和词典查找策略。
3. 实验或效果：微调Qwen3-14B模型在测试集上获得最佳官方分数0.678，多方法表现竞争性，为类似任务提供见解。

## 📄 摘要（原文）

> The ChemoTimelines shared task benchmarks methods for constructing timelines of systemic anticancer treatment from electronic health records of cancer patients. This paper describes our methods, results, and findings for subtask 2 -- generating patient chemotherapy timelines from raw clinical notes. We evaluated strategies involving chain-of-thought thinking, supervised fine-tuning, direct preference optimization, and dictionary-based lookup to improve timeline extraction. All of our approaches followed a two-step workflow, wherein an LLM first extracted chemotherapy events from individual clinical notes, and then an algorithm normalized and aggregated events into patient-level timelines. Each specific method differed in how the associated LLM was utilized and trained. Multiple approaches yielded competitive performances on the test set leaderboard, with fine-tuned Qwen3-14B achieving the best official score of 0.678. Our results and analyses could provide useful insights for future attempts on this task as well as the design of similar tasks.

