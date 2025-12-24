---
layout: default
title: "CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal"
---

# CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19554" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19554v1</a>
  <a href="https://arxiv.org/pdf/2512.19554.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19554v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19554v1', 'CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yongxin Wang, Zhicheng Yang, Meng Cao, Mingfei Han, Haokun Lin, Yingying Zhu, Xiaojun Chang, Xiaodan Liang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**CARE：面向可验证多模态推理，通过对比锚定反射改进失败案例学习。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `对比学习` `强化学习` `失败案例学习` `视觉问答` `自修复` `可验证性`

## 📋 核心要点

1. 现有RLVR方法在处理失败案例时存在不足，未能充分利用错误数据中的信息，导致梯度停滞或信用分配错误。
2. CARE框架通过对比学习和反射引导重采样，将失败案例转化为有效的监督信号，从而提升模型的多模态推理能力。
3. 实验表明，CARE在多个视觉推理基准测试中显著提升了模型准确率，并在MathVista和MMMU-Pro上取得了领先水平。

## 📝 摘要（中文）

具有可验证奖励的群体相对强化学习（RLVR）常常浪费了最有用的数据——失败案例。当所有rollout都是错误时，梯度会停滞；当一个rollout碰巧是正确的，更新通常会忽略其他接近但错误的rollout，并且信用可能被错误地分配给虚假链。我们提出了CARE（对比锚定反射），一个以失败为中心的后训练框架，用于多模态推理，将错误转化为监督。CARE结合了：（i）锚定对比目标，围绕最佳rollout形成一个紧凑的子群，以及一组语义上接近的难负例，执行子群内的z-score归一化，仅对负例进行缩放，并包含一个全负例救援以防止零信号批次；（ii）反射引导重采样（RGR），一种一次性的结构化自修复，重写一个具有代表性的失败案例，并使用相同的验证器重新评分，将接近的失败转化为可用的正例，而无需任何测试时反射。CARE提高了准确性和训练平滑性，同时明确增加了来自失败案例的学习信号份额。在Qwen2.5-VL-7B上，CARE在六个可验证的视觉推理基准测试中，将宏平均准确率提高了4.6个百分点；在Qwen3-VL-8B上，在相同的评估协议下，它在MathVista和MMMU-Pro上达到了有竞争力的或最先进的结果。

## 🔬 方法详解

**问题定义**：现有的群体相对强化学习与可验证奖励（RLVR）方法在处理多模态推理任务时，未能充分利用失败的rollout数据。当所有rollout都错误时，梯度更新停滞；即使存在正确的rollout，也往往忽略了其他接近但错误的rollout所包含的信息，导致信用分配不准确，影响模型学习效率和最终性能。

**核心思路**：CARE的核心思路是将失败案例转化为有效的监督信号，从而提升模型的多模态推理能力。通过对比学习，模型能够区分正确的rollout和接近但错误的rollout，并学习到失败的原因。反射引导重采样则将接近的失败案例转化为可用的正例，进一步增强了模型的学习能力。

**技术框架**：CARE是一个后训练框架，主要包含两个核心模块：锚定对比学习和反射引导重采样（RGR）。首先，锚定对比学习模块围绕最佳rollout构建一个紧凑的子群，并引入语义上接近的难负例，通过z-score归一化和负例缩放，增强对比学习的效果。其次，RGR模块通过重写具有代表性的失败案例，并使用相同的验证器重新评分，将接近的失败转化为可用的正例。

**关键创新**：CARE的关键创新在于其以失败为中心的学习范式，以及将对比学习和反射引导重采样相结合的方法。与传统的RLVR方法不同，CARE充分利用了失败案例中的信息，将其转化为有效的监督信号，从而提升了模型的学习效率和泛化能力。此外，RGR模块通过结构化的自修复，有效地解决了数据稀疏的问题。

**关键设计**：在锚定对比学习中，关键的设计包括如何选择合适的锚点（最佳rollout）、如何构建难负例集合，以及如何进行z-score归一化和负例缩放。在反射引导重采样中，关键的设计包括如何选择具有代表性的失败案例进行重写，以及如何保证重写后的rollout仍然具有可验证性。此外，全负例救援机制用于处理零信号批次，保证训练的稳定性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19554v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19554v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19554v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

CARE在Qwen2.5-VL-7B模型上，于六个可验证的视觉推理基准测试中，宏平均准确率提升了4.6个百分点。在Qwen3-VL-8B模型上，CARE在MathVista和MMMU-Pro数据集上达到了具有竞争力的或最先进的结果，证明了其在多模态推理任务上的有效性。

## 🎯 应用场景

CARE框架可应用于各种需要多模态推理和可验证性的任务，例如视觉问答、机器人导航、智能对话系统等。该研究有助于提升AI系统的可靠性和安全性，使其能够更好地理解和处理复杂的多模态信息，并做出更准确的决策。未来，该方法有望在自动驾驶、医疗诊断等领域发挥重要作用。

## 📄 摘要（原文）

> Group-relative reinforcement learning with verifiable rewards (RLVR) often wastes the most informative data it already has the failures. When all rollouts are wrong, gradients stall; when one happens to be correct, the update usually ignores why the others are close-but-wrong, and credit can be misassigned to spurious chains. We present CARE (Contrastive Anchored REflection), a failure-centric post-training framework for multimodal reasoning that turns errors into supervision. CARE combines: (i) an anchored-contrastive objective that forms a compact subgroup around the best rollout and a set of semantically proximate hard negatives, performs within-subgroup z-score normalization with negative-only scaling, and includes an all-negative rescue to prevent zero-signal batches; and (ii) Reflection-Guided Resampling (RGR), a one-shot structured self-repair that rewrites a representative failure and re-scores it with the same verifier, converting near-misses into usable positives without any test-time reflection. CARE improves accuracy and training smoothness while explicitly increasing the share of learning signal that comes from failures. On Qwen2.5-VL-7B, CARE lifts macro-averaged accuracy by 4.6 points over GRPO across six verifiable visual-reasoning benchmarks; with Qwen3-VL-8B it reaches competitive or state-of-the-art results on MathVista and MMMU-Pro under an identical evaluation protocol.

