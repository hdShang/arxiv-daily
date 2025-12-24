---
layout: default
title: Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study
---

# Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14185" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14185v2</a>
  <a href="https://arxiv.org/pdf/2505.14185.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14185v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14185v2', 'Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaustubh Ponkshe, Shaan Shah, Raghav Singhal, Praneeth Vepakomma

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-20 (更新: 2025-10-04)

**备注**: Kaustubh Ponkshe, Shaan Shah, and Raghav Singhal contributed equally to this work

**🔗 代码/项目**: [GITHUB](https://github.com/CERT-Lab/safety-subspaces)

---

## 💡 一句话要点

**研究安全子空间与线性独立性，揭示模型安全性挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `安全对齐` `大型语言模型` `微调策略` `激活模式` `对抗性训练`

## 📋 核心要点

1. 现有方法在安全对齐方面存在脆弱性，微调后可能导致有害行为的重新出现。
2. 论文通过实证研究探讨安全行为与通用学习的关系，提出安全性与学习组件高度纠缠的观点。
3. 研究在五个开源LLM上进行实验，验证了安全性与有用性行为的重叠性，提出了新的防御策略需求。

## 📝 摘要（中文）

大型语言模型（LLMs）依赖安全对齐以生成社会可接受的响应。然而，这种行为往往脆弱：即使在良性或轻度污染的数据上进行进一步微调，也可能导致安全性下降并重新引入有害行为。本文通过实证研究探讨安全行为是否集中在特定线性子空间，是否可以与通用学习分离，以及有害性是否源于可区分的激活模式。研究发现，放大安全行为的子空间同样放大有用行为，且不同安全含义的提示激活重叠的表示。这表明安全性与模型的通用学习组件高度纠缠，强调了基于子空间的防御面临的根本限制，并指出需要替代策略以在持续训练中保持安全性。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在安全对齐方面的脆弱性，现有方法在微调后可能导致安全性下降和有害行为的重新出现。

**核心思路**：通过实证研究，探讨安全行为是否集中在特定线性子空间，揭示安全性与通用学习组件的高度纠缠，强调基于子空间的防御策略的局限性。

**技术框架**：研究采用了多种实验方法，分析了五个开源LLM（如Llama和Qwen系列）的权重和激活空间，比较了安全行为与有用行为的重叠性。

**关键创新**：最重要的创新在于发现安全性并不在独立的线性子空间中，而是与模型的通用学习组件高度纠缠，这与现有理论相悖。

**关键设计**：实验中使用了多种微调策略和数据集，重点关注权重和激活模式的分析，确保结果的可靠性和可重复性。实验代码已公开，便于后续研究者验证和扩展。

## 📊 实验亮点

实验结果表明，安全行为与有用行为在权重和激活空间中高度重叠，提示不同安全含义的输入激活相似的表示。这一发现挑战了传统的安全子空间理论，强调了基于子空间的防御策略的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的安全性提升、对抗性训练和模型微调策略的优化。通过深入理解安全性与通用学习的关系，研究为开发更稳健的AI系统提供了理论基础，未来可能影响AI在社会应用中的安全性和可靠性。

## 📄 摘要（原文）

> Large Language Models (LLMs) rely on safety alignment to produce socially acceptable responses. However, this behavior is known to be brittle: further fine-tuning, even on benign or lightly contaminated data, can degrade safety and reintroduce harmful behaviors. A growing body of work suggests that alignment may correspond to identifiable directions in weight space, forming subspaces that could, in principle, be isolated or preserved to defend against misalignment. In this work, we conduct a comprehensive empirical study of this perspective. We examine whether safety-relevant behavior is concentrated in specific linear subspaces, whether it can be separated from general-purpose learning, and whether harmfulness arises from distinguishable patterns in activations. Across both weight and activation spaces, our findings are consistent: subspaces that amplify safe behaviors also amplify useful ones, and prompts with different safety implications activate overlapping representations. Rather than residing in distinct directions, we show that safety is highly entangled with the general learning components of the model. This suggests that subspace-based defenses face fundamental limitations and underscores the need for alternative strategies to preserve safety under continued training. We corroborate these findings with multiple experiments on five open-source LLMs from the Llama and Qwen families. Our code is publicly available at: https://github.com/CERT-Lab/safety-subspaces.

