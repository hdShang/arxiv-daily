---
layout: default
title: All You Need Are Random Visual Tokens? Demystifying Token Pruning in VLLMs
---

# All You Need Are Random Visual Tokens? Demystifying Token Pruning in VLLMs

**arXiv**: [2512.07580v1](https://arxiv.org/abs/2512.07580) | [PDF](https://arxiv.org/pdf/2512.07580.pdf)

**作者**: Yahong Wang, Juncheng Wu, Zhangkai Ni, Longzhen Yang, Yihang Liu, Chengmei Yang, Ying Wen, Xianfeng Tang, Hui Liu, Yuyin Zhou, Lianghua He

---

## 💡 一句话要点

**提出信息地平线概念，揭示视觉令牌在深层冗余，通过随机剪枝提升VLLM效率**

**关键词**: `视觉大语言模型` `令牌剪枝` `信息地平线` `随机剪枝` `计算效率` `视觉令牌冗余`

## 📋 核心要点

1. 发现现有训练无关剪枝方法在深层表现不优于随机剪枝，归因于令牌信息消失
2. 提出信息度量分析视觉令牌信息变化，识别信息地平线，其位置随任务和模型能力变化
3. 实验表明深层随机剪枝有效平衡性能与效率，结合DivPrune在Qwen2.5-VL上剪枝50%保持96.9%性能

## 📄 摘要（原文）

> Vision Large Language Models (VLLMs) incur high computational costs due to their reliance on hundreds of visual tokens to represent images. While token pruning offers a promising solution for accelerating inference, this paper, however, identifies a key observation: in deeper layers (e.g., beyond the 20th), existing training-free pruning methods perform no better than random pruning. We hypothesize that this degradation is caused by "vanishing token information", where visual tokens progressively lose their salience with increasing network depth. To validate this hypothesis, we quantify a token's information content by measuring the change in the model output probabilities upon its removal. Using this proposed metric, our analysis of the information of visual tokens across layers reveals three key findings: (1) As layers deepen, the information of visual tokens gradually becomes uniform and eventually vanishes at an intermediate layer, which we term as "information horizon", beyond which the visual tokens become redundant; (2) The position of this horizon is not static; it extends deeper for visually intensive tasks, such as Optical Character Recognition (OCR), compared to more general tasks like Visual Question Answering (VQA); (3) This horizon is also strongly correlated with model capacity, as stronger VLLMs (e.g., Qwen2.5-VL) employ deeper visual tokens than weaker models (e.g., LLaVA-1.5). Based on our findings, we show that simple random pruning in deep layers efficiently balances performance and efficiency. Moreover, integrating random pruning consistently enhances existing methods. Using DivPrune with random pruning achieves state-of-the-art results, maintaining 96.9% of Qwen-2.5-VL-7B performance while pruning 50% of visual tokens. The code will be publicly available at https://github.com/YahongWang1/Information-Horizon.

