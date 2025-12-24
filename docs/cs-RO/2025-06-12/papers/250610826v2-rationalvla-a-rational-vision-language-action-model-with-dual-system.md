---
layout: default
title: "RationalVLA: A Rational Vision-Language-Action Model with Dual System"
---

# RationalVLA: A Rational Vision-Language-Action Model with Dual System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10826" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10826v2</a>
  <a href="https://arxiv.org/pdf/2506.10826.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10826v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10826v2', 'RationalVLA: A Rational Vision-Language-Action Model with Dual System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenxuan Song, Jiayi Chen, Wenxue Li, Xu He, Han Zhao, Can Cui, Pengxiang Ding Shiyan Su, Feilong Tang, Xuelian Cheng, Donglin Wang, Zongyuan Ge, Xinhu Zheng, Zhe Liu, Hesheng Wang, Haoang Li

**分类**: cs.RO

**发布日期**: 2025-06-12 (更新: 2025-06-13)

**备注**: 14 pages

**🔗 代码/项目**: [PROJECT_PAGE](https://irpn-eai.github.io/RationalVLA)

---

## 💡 一句话要点

**提出RationalVLA以解决机器人对自然语言指令理解不足的问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `自然语言处理` `多模态学习` `视觉语言模型` `鲁棒性` `指令推理` `潜在空间嵌入`

## 📋 核心要点

1. 现有方法假设指令与环境完美对齐，导致在模糊或不可行指令下的鲁棒性和泛化能力不足。
2. 提出RationalVLA模型，通过引入可学习的潜在空间嵌入，将视觉语言模型与操作策略结合，增强指令推理和执行能力。
3. RationalVLA在RAMA基准上成功率提升14.5%，并在标准操作任务中表现出竞争力，验证了其实用性和鲁棒性。

## 📝 摘要（中文）

现实世界中，机器人需要理解和响应自然语言指令，但现有的语言条件下的操作任务通常假设指令与环境完美对齐，这限制了其在模糊或不可行指令下的鲁棒性和泛化能力。为此，本文引入了Rational Manipulation (RAMA)基准，构建了一个包含14000多个样本的数据集，涵盖六个维度的缺陷指令。我们提出了Rational Vision-Language-Action模型（RationalVLA），它通过引入可学习的潜在空间嵌入，将高层视觉语言模型与低层操作策略集成，能够有效推理指令、拒绝不可行命令并执行操作。实验表明，RationalVLA在RAMA基准上成功率提高了14.5%，并在标准操作任务中保持竞争力。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在处理自然语言指令时的理解和执行能力不足的问题。现有方法通常假设指令与环境完美对齐，这在现实场景中往往不成立，导致机器人在面对模糊或不可行指令时表现不佳。

**核心思路**：论文提出RationalVLA模型，核心在于将高层视觉语言模型与低层操作策略结合，通过引入可学习的潜在空间嵌入，使模型能够有效推理指令并拒绝不可行的命令。这样的设计使得模型在复杂环境中更具适应性。

**技术框架**：RationalVLA的整体架构包括两个主要模块：高层的视觉语言理解模块和低层的操作策略模块。高层模块负责解析自然语言指令并提取相关视觉信息，而低层模块则负责具体的操作执行。两个模块通过潜在空间嵌入进行交互，形成闭环反馈。

**关键创新**：RationalVLA的关键创新在于其双系统设计，能够在面对未见过的指令和缺陷指令时进行有效推理和拒绝。这一设计与现有方法的本质区别在于其增强了模型的鲁棒性和泛化能力。

**关键设计**：模型的关键设计包括潜在空间嵌入的学习机制，以及针对不同类型指令的损失函数设置。这些设计确保了模型在执行过程中能够灵活应对多样化的指令和环境变化。通过这些技术细节，RationalVLA在复杂场景中表现出色。

## 📊 实验亮点

在RAMA基准上，RationalVLA模型的成功率比现有最先进的方法提高了14.5%，并且在平均任务长度上表现出0.94的优势。此外，模型在标准操作任务中也保持了竞争力，验证了其在实际应用中的有效性和鲁棒性。

## 🎯 应用场景

RationalVLA模型具有广泛的应用潜力，特别是在智能家居、服务机器人和工业自动化等领域。其能够理解和执行自然语言指令的能力，将大大提升人机交互的自然性和效率，推动机器人技术在实际应用中的普及和发展。

## 📄 摘要（原文）

> A fundamental requirement for real-world robotic deployment is the ability to understand and respond to natural language instructions. Existing language-conditioned manipulation tasks typically assume that instructions are perfectly aligned with the environment. This assumption limits robustness and generalization in realistic scenarios where instructions may be ambiguous, irrelevant, or infeasible. To address this problem, we introduce RAtional MAnipulation (RAMA), a new benchmark that challenges models with both unseen executable instructions and defective ones that should be rejected. In RAMA, we construct a dataset with over 14,000 samples, including diverse defective instructions spanning six dimensions: visual, physical, semantic, motion, safety, and out-of-context. We further propose the Rational Vision-Language-Action model (RationalVLA). It is a dual system for robotic arms that integrates the high-level vision-language model with the low-level manipulation policy by introducing learnable latent space embeddings. This design enables RationalVLA to reason over instructions, reject infeasible commands, and execute manipulation effectively. Experiments demonstrate that RationalVLA outperforms state-of-the-art baselines on RAMA by a 14.5% higher success rate and 0.94 average task length, while maintaining competitive performance on standard manipulation tasks. Real-world trials further validate its effectiveness and robustness in practical applications. Our project page is https://irpn-eai.github.io/RationalVLA.

