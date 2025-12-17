---
layout: default
title: IRG-MotionLLM: Interleaving Motion Generation, Assessment and Refinement for Text-to-Motion Generation
---

# IRG-MotionLLM: Interleaving Motion Generation, Assessment and Refinement for Text-to-Motion Generation

**arXiv**: [2512.10730v1](https://arxiv.org/abs/2512.10730) | [PDF](https://arxiv.org/pdf/2512.10730.pdf)

**作者**: Yuan-Ming Li, Qize Yang, Nan Lei, Shenghao Fu, Ling-An Zeng, Jian-Fang Hu, Xihan Wei, Wei-Shi Zheng

---

## 💡 一句话要点

**提出IRG-MotionLLM模型，通过交织运动生成、评估与精炼提升文本到运动生成性能。**

**关键词**: `文本到运动生成` `运动评估` `运动精炼` `大语言模型` `迭代对话` `数据合成`

## 📋 核心要点

1. 核心问题：现有运动感知大语言模型将理解与生成分离，缺乏任务间交互反馈。
2. 方法要点：引入IRMoGen范式，通过迭代文本-运动对话紧密耦合生成、评估与精炼。
3. 实验或效果：模型在标准基准上优于基线，评估与精炼任务显著改善文本-运动对齐。

## 📄 摘要（原文）

> Recent advances in motion-aware large language models have shown remarkable promise for unifying motion understanding and generation tasks. However, these models typically treat understanding and generation separately, limiting the mutual benefits that could arise from interactive feedback between tasks. In this work, we reveal that motion assessment and refinement tasks act as crucial bridges to enable bidirectional knowledge flow between understanding and generation. Leveraging this insight, we propose Interleaved Reasoning for Motion Generation (IRMoGen), a novel paradigm that tightly couples motion generation with assessment and refinement through iterative text-motion dialogue. To realize this, we introduce IRG-MotionLLM, the first model that seamlessly interleaves motion generation, assessment, and refinement to improve generation performance. IRG-MotionLLM is developed progressively with a novel three-stage training scheme, initializing and subsequently enhancing native IRMoGen capabilities. To facilitate this development, we construct an automated data engine to synthesize interleaved reasoning annotations from existing text-motion datasets. Extensive experiments demonstrate that: (i) Assessment and refinement tasks significantly improve text-motion alignment; (ii) Interleaving motion generation, assessment, and refinement steps yields consistent performance gains across training stages; and (iii) IRG-MotionLLM clearly outperforms the baseline model and achieves advanced performance on standard text-to-motion generation benchmarks. Cross-evaluator testing further validates its effectiveness. Code & Data: https://github.com/HumanMLLM/IRG-MotionLLM/tree/main.

