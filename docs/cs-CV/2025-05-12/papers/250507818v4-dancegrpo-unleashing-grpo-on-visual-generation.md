---
layout: default
title: "DanceGRPO: Unleashing GRPO on Visual Generation"
---

# DanceGRPO: Unleashing GRPO on Visual Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07818" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07818v4</a>
  <a href="https://arxiv.org/pdf/2505.07818.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07818v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07818v4', 'DanceGRPO: Unleashing GRPO on Visual Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyue Xue, Jie Wu, Yu Gao, Fangyuan Kong, Lingting Zhu, Mengzhao Chen, Zhiheng Liu, Wei Liu, Qiushan Guo, Weilin Huang, Ping Luo

**分类**: cs.CV

**发布日期**: 2025-05-12 (更新: 2025-08-28)

**备注**: Project Page: https://dancegrpo.github.io/

---

## 💡 一句话要点

**提出DanceGRPO以解决视觉生成中的优化稳定性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成式人工智能` `视觉生成` `强化学习` `策略优化` `人类反馈对齐`

## 📋 核心要点

1. 现有的强化学习方法在处理大规模多样化提示集时，优化过程不稳定，限制了其实用性。
2. DanceGRPO通过创新性地适应GRPO，利用其内在的稳定机制来克服视觉生成中的优化挑战。
3. 实验结果显示，DanceGRPO在多个基准测试中表现优异，性能提升可达181%，展现出强大的适应性和稳定性。

## 📝 摘要（中文）

近年来，生成式人工智能的进步彻底改变了视觉内容的创作，但如何将模型输出与人类偏好对齐仍然是一个关键挑战。尽管强化学习（RL）已成为微调生成模型的有前景的方法，但现有方法如DDPO和DPOK在面对大规模多样化提示集时存在优化不稳定的根本限制。本文提出了DanceGRPO，一个通过创新性地将组相对策略优化（GRPO）适应于视觉生成任务来解决这些限制的框架。DanceGRPO在多个现代生成范式中展示了稳定的策略优化，并在复杂的真实场景中保持强大的性能。实验结果表明，DanceGRPO在多个基准测试中超越基线方法，提升幅度可达181%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法在视觉生成任务中优化不稳定的问题，尤其是在面对大规模和多样化的提示集时，现有方法如DDPO和DPOK表现不佳。

**核心思路**：DanceGRPO的核心思路是将组相对策略优化（GRPO）应用于视觉生成任务，利用其内在的稳定机制来提高优化的稳定性和一致性。

**技术框架**：DanceGRPO框架包括多个模块，首先是策略优化模块，接着是与人类反馈对齐的奖励模型，最后是生成模型的训练与评估。

**关键创新**：DanceGRPO的主要创新在于其稳定的策略优化能力，能够在多种生成模型（如扩散模型和修正流）中保持一致的性能，这与现有方法的优化不稳定性形成鲜明对比。

**关键设计**：在设计上，DanceGRPO采用了多种奖励模型来捕捉人类偏好，包括图像/视频美学、文本-图像对齐、视频运动质量等，确保优化过程能够适应多样化的反馈。具体的损失函数和网络结构细节在论文中有详细描述。

## 📊 实验亮点

DanceGRPO在多个基准测试中表现出色，相较于基线方法，性能提升可达181%。在HPS-v2.1、CLIP Score、VideoAlign和GenEval等多个指标上均超越了现有方法，证明了其在视觉生成任务中的有效性和稳定性。

## 🎯 应用场景

DanceGRPO的研究成果在多个领域具有潜在应用价值，包括电影制作、游戏开发和广告创意等视觉内容生成场景。通过优化生成模型与人类偏好的对齐，DanceGRPO能够提升视觉内容的质量和吸引力，推动创意产业的发展。未来，该方法还可能扩展到其他生成任务，如文本生成和音频合成等。

## 📄 摘要（原文）

> Recent advances in generative AI have revolutionized visual content creation, yet aligning model outputs with human preferences remains a critical challenge. While Reinforcement Learning (RL) has emerged as a promising approach for fine-tuning generative models, existing methods like DDPO and DPOK face fundamental limitations - particularly their inability to maintain stable optimization when scaling to large and diverse prompt sets, severely restricting their practical utility. This paper presents DanceGRPO, a framework that addresses these limitations through an innovative adaptation of Group Relative Policy Optimization (GRPO) for visual generation tasks. Our key insight is that GRPO's inherent stability mechanisms uniquely position it to overcome the optimization challenges that plague prior RL-based approaches on visual generation. DanceGRPO establishes several significant advances: First, it demonstrates consistent and stable policy optimization across multiple modern generative paradigms, including both diffusion models and rectified flows. Second, it maintains robust performance when scaling to complex, real-world scenarios encompassing three key tasks and four foundation models. Third, it shows remarkable versatility in optimizing for diverse human preferences as captured by five distinct reward models assessing image/video aesthetics, text-image alignment, video motion quality, and binary feedback. Our comprehensive experiments reveal that DanceGRPO outperforms baseline methods by up to 181\% across multiple established benchmarks, including HPS-v2.1, CLIP Score, VideoAlign, and GenEval. Our results establish DanceGRPO as a robust and versatile solution for scaling Reinforcement Learning from Human Feedback (RLHF) tasks in visual generation, offering new insights into harmonizing reinforcement learning and visual synthesis.

