---
layout: default
title: "Omni-DPO: A Dual-Perspective Paradigm for Dynamic Preference Learning of LLMs"
---

# Omni-DPO: A Dual-Perspective Paradigm for Dynamic Preference Learning of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10054" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10054v2</a>
  <a href="https://arxiv.org/pdf/2506.10054.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10054v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10054v2', 'Omni-DPO: A Dual-Perspective Paradigm for Dynamic Preference Learning of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shangpin Peng, Weinong Wang, Zhuotao Tian, Senqiao Yang, Xing Wu, Haotian Xu, Chengquan Zhang, Takashi Isobe, Baotian Hu, Min Zhang

**分类**: cs.LG, cs.AI, cs.CL, cs.CV

**发布日期**: 2025-06-11 (更新: 2025-08-15)

**🔗 代码/项目**: [GITHUB](https://github.com/pspdada/Omni-DPO)

---

## 💡 一句话要点

**提出Omni-DPO以解决动态偏好学习中的数据利用问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `动态偏好学习` `直接偏好优化` `人类反馈强化学习` `模型性能优化` `自适应加权` `文本理解` `数学推理` `深度学习`

## 📋 核心要点

1. 现有DPO方法未能充分利用偏好对的内在质量和学习效用，导致性能不佳。
2. Omni-DPO通过双视角优化框架，结合偏好对的质量和模型的学习动态，提升数据利用效率。
3. 实验结果显示，Omni-DPO在文本理解和数学推理任务中均显著超越基线方法，验证了其有效性。

## 📝 摘要（中文）

直接偏好优化（DPO）因其简单高效成为人类反馈强化学习（RLHF）的基石。然而，现有DPO方法通常均匀对待所有偏好对，忽视其内在质量和学习效用的关键差异，导致数据利用和性能的次优。为此，本文提出Omni-DPO，一个双视角优化框架，联合考虑每个偏好对的内在质量和模型在这些偏好对上的演变性能。通过根据数据质量和模型学习动态自适应加权样本，Omni-DPO实现了更有效的训练数据利用，并取得了更好的性能。实验结果表明，Omni-DPO在多个模型和基准上表现优越，尤其在文本理解任务中，使用Omni-DPO微调的Gemma-2-9b-it在Arena-Hard基准上比领先的LLM Claude 3 Opus高出6.7分。

## 🔬 方法详解

**问题定义**：本文旨在解决现有DPO方法在处理偏好对时的均匀对待问题，导致数据利用不充分和性能下降。

**核心思路**：Omni-DPO通过双视角框架，分别考虑偏好对的内在质量和模型的学习动态，采用自适应加权策略来优化训练过程。

**技术框架**：Omni-DPO的整体架构包括数据质量评估模块和模型性能监控模块，二者共同影响样本的加权策略，从而优化训练数据的选择和使用。

**关键创新**：Omni-DPO的创新之处在于其双视角优化策略，区别于传统方法的均匀处理方式，使得训练过程更加高效和灵活。

**关键设计**：在参数设置上，Omni-DPO引入了动态加权机制，损失函数设计考虑了样本的质量和模型的学习进度，确保训练过程的适应性和有效性。

## 📊 实验亮点

在实验中，使用Omni-DPO微调的Gemma-2-9b-it在Arena-Hard基准上比Claude 3 Opus高出6.7分，显示出显著的性能提升。此外，在数学推理任务中，Omni-DPO在所有基准上均超越了基线方法，证明了其有效性和鲁棒性。

## 🎯 应用场景

Omni-DPO的研究成果在多个领域具有潜在应用价值，尤其是在需要从人类反馈中学习的任务中，如对话系统、推荐系统和自动内容生成等。通过提升模型对偏好数据的利用效率，未来可以实现更智能的交互和更高质量的生成内容。

## 📄 摘要（原文）

> Direct Preference Optimization (DPO) has become a cornerstone of reinforcement learning from human feedback (RLHF) due to its simplicity and efficiency. However, existing DPO-based approaches typically treat all preference pairs uniformly, ignoring critical variations in their inherent quality and learning utility, leading to suboptimal data utilization and performance. To address this challenge, we propose Omni-DPO, a dual-perspective optimization framework that jointly accounts for (1) the inherent quality of each preference pair and (2) the model's evolving performance on those pairs. By adaptively weighting samples according to both data quality and the model's learning dynamics during training, Omni-DPO enables more effective training data utilization and achieves better performance. Experimental results on various models and benchmarks demonstrate the superiority and generalization capabilities of Omni-DPO. On textual understanding tasks, Gemma-2-9b-it finetuned with Omni-DPO beats the leading LLM, Claude 3 Opus, by a significant margin of 6.7 points on the Arena-Hard benchmark. On mathematical reasoning tasks, Omni-DPO consistently outperforms the baseline methods across all benchmarks, providing strong empirical evidence for the effectiveness and robustness of our approach. Code and models will be available at https://github.com/pspdada/Omni-DPO.

