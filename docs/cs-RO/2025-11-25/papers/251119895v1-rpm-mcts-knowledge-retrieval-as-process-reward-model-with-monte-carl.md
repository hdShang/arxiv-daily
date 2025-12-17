---
layout: default
title: RPM-MCTS: Knowledge-Retrieval as Process Reward Model with Monte Carlo Tree Search for Code Generation
---

# RPM-MCTS: Knowledge-Retrieval as Process Reward Model with Monte Carlo Tree Search for Code Generation

**arXiv**: [2511.19895v1](https://arxiv.org/abs/2511.19895) | [PDF](https://arxiv.org/pdf/2511.19895.pdf)

**作者**: Yuanyuan Lin, Xiangyu Ouyang, Teng Zhang, Kaixin Sui

---

## 💡 一句话要点

**提出RPM-MCTS方法以解决代码生成中中间步骤评估难和错误定位问题**

**关键词**: `代码生成` `蒙特卡洛树搜索` `过程奖励模型` `知识检索` `沙箱执行` `令牌优化`

## 📋 核心要点

1. 核心问题：树搜索方法难以评估中间算法步骤，无法及时纠正错误，导致代码错误和计算成本高。
2. 方法要点：利用知识检索作为过程奖励模型，结合MCTS评估步骤，过滤冗余节点并使用沙箱反馈定位错误。
3. 实验或效果：在四个基准测试中优于现有方法，减少约15%令牌消耗，微调后提升模型代码能力。

## 📄 摘要（原文）

> Tree search-based methods have made significant progress in enhancing the code generation capabilities of large language models. However, due to the difficulty in effectively evaluating intermediate algorithmic steps and the inability to locate and timely correct erroneous steps, these methods often generate incorrect code and incur increased computational costs. To tackle these problems, we propose RPM-MCTS, an effective method that utilizes Knowledge-Retrieval as Process Reward Model based on Monte Carlo Tree Search to evaluate intermediate algorithmic steps. By utilizing knowledge base retrieval, RPM-MCTS avoids the complex training of process reward models. During the expansion phase, similarity filtering is employed to remove redundant nodes, ensuring diversity in reasoning paths. Furthermore, our method utilizes sandbox execution feedback to locate erroneous algorithmic steps during generation, enabling timely and targeted corrections. Extensive experiments on four public code generation benchmarks demonstrate that RPM-MCTS outperforms current state-of-the-art methods while achieving an approximately 15% reduction in token consumption. Furthermore, full fine-tuning of the base model using the data constructed by RPM-MCTS significantly enhances its code capabilities.

