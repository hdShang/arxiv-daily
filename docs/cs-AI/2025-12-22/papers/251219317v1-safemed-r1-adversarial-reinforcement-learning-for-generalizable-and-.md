---
layout: default
title: "SafeMed-R1: Adversarial Reinforcement Learning for Generalizable and Robust Medical Reasoning in Vision-Language Models"
---

# SafeMed-R1: Adversarial Reinforcement Learning for Generalizable and Robust Medical Reasoning in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19317" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19317v1</a>
  <a href="https://arxiv.org/pdf/2512.19317.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19317v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19317v1', 'SafeMed-R1: Adversarial Reinforcement Learning for Generalizable and Robust Medical Reasoning in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: A. A. Gde Yogi Pramana, Jason Ray, Anthony Jaya, Michael Wijaya

**分类**: cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**SafeMed-R1：用于视觉-语言模型中可泛化和鲁棒医学推理的对抗强化学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学视觉问答` `对抗攻击` `对抗训练` `强化学习` `鲁棒性` `视觉-语言模型` `群体相对策略优化` `随机平滑`

## 📋 核心要点

1. 现有的视觉-语言模型在医学视觉问答中易受对抗攻击，标准对抗训练降低了泛化性和推理质量。
2. SafeMed-R1通过结合对抗训练与群体相对策略优化，并在推理时使用随机平滑，增强模型的鲁棒性。
3. 实验表明，SafeMed-R1在对抗攻击下比标准微调VLM的鲁棒性提高了59个百分点，且思维链推理模型更鲁棒。

## 📝 摘要（中文）

视觉-语言模型(VLM)在医学视觉问答(VQA)方面显示出巨大的潜力，但其在临床环境中的部署受到对抗攻击严重脆弱性的阻碍。标准的对抗训练虽然对简单的任务有效，但通常会降低泛化性能和生成的临床推理质量。我们引入了SafeMed-R1，一个混合防御框架，它确保了鲁棒的性能，同时保持高质量、可解释的医学推理。SafeMed-R1采用两阶段方法：在训练时，我们将对抗训练与群体相对策略优化(AT-GRPO)相结合，以显式地增强推理过程，使其免受最坏情况的扰动；在推理时，我们使用随机平滑来增强模型，以提供经过认证的$L_2$-范数鲁棒性保证。我们在OmniMedVQA基准上评估了SafeMed-R1，该基准涵盖了八种医学成像模式，包含超过88,000个样本。我们的实验表明，标准的微调VLM虽然在干净的输入上达到了95%的准确率，但在PGD攻击下会崩溃到大约25%。相比之下，SafeMed-R1在相同的对抗条件下保持了84.45%的准确率，代表了鲁棒性提高了59个百分点。此外，我们证明了使用显式思维链推理训练的模型比仅使用指令的变体表现出更强的对抗鲁棒性，这表明医学人工智能系统中可解释性和安全性之间存在协同作用。

## 🔬 方法详解

**问题定义**：论文旨在解决医学视觉问答（Medical VQA）中，视觉-语言模型（VLM）容易受到对抗攻击的问题。现有方法，如标准对抗训练，虽然能提高鲁棒性，但会牺牲模型的泛化能力和推理质量，导致在实际临床应用中效果不佳。

**核心思路**：论文的核心思路是结合对抗训练和强化学习，设计一个混合防御框架SafeMed-R1，在训练阶段增强模型对对抗样本的鲁棒性，同时保持其泛化能力和推理质量。此外，在推理阶段使用随机平滑技术，提供经过认证的鲁棒性保证。

**技术框架**：SafeMed-R1框架包含两个主要阶段：训练阶段和推理阶段。在训练阶段，使用对抗训练与群体相对策略优化（AT-GRPO）相结合的方法，显式地增强推理过程，使其免受最坏情况的扰动。在推理阶段，使用随机平滑技术来增强模型，以提供经过认证的$L_2$-范数鲁棒性保证。

**关键创新**：论文的关键创新在于将对抗训练与群体相对策略优化相结合，用于增强医学视觉问答模型的鲁棒性。与传统的对抗训练方法相比，AT-GRPO能够更好地平衡模型的鲁棒性和泛化能力，同时保持高质量的临床推理。此外，论文还证明了使用显式思维链推理训练的模型具有更强的对抗鲁棒性。

**关键设计**：AT-GRPO的具体实现细节未知，但可以推测其目标是优化策略，使得模型在对抗样本上的表现尽可能接近在干净样本上的表现。随机平滑的具体参数设置未知，但其目的是通过对输入进行随机扰动，并对模型的输出进行平均，从而提高模型的鲁棒性。论文中使用的损失函数和网络结构等技术细节未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19317v1/general_ovvw.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19317v1/example.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SafeMed-R1在OmniMedVQA基准测试中表现出色，在PGD攻击下，标准微调VLM的准确率从95%下降到25%，而SafeMed-R1保持了84.45%的准确率，鲁棒性提高了59个百分点。此外，实验还表明，使用显式思维链推理训练的模型比仅使用指令的变体表现出更强的对抗鲁棒性。

## 🎯 应用场景

SafeMed-R1的研究成果可应用于医疗影像诊断、辅助决策等领域，提高医学人工智能系统的安全性和可靠性。通过增强模型对对抗攻击的防御能力，可以避免恶意攻击者篡改诊断结果，保障患者的权益。该研究还有助于推动医学人工智能在临床环境中的广泛应用，提升医疗服务的质量和效率。

## 📄 摘要（原文）

> Vision--Language Models (VLMs) show significant promise for Medical Visual Question Answering (VQA), yet their deployment in clinical settings is hindered by severe vulnerability to adversarial attacks. Standard adversarial training, while effective for simpler tasks, often degrades both generalization performance and the quality of generated clinical reasoning. We introduce SafeMed-R1, a hybrid defense framework that ensures robust performance while preserving high-quality, interpretable medical reasoning. SafeMed-R1 employs a two-stage approach: at training time, we integrate Adversarial Training with Group Relative Policy Optimization (AT-GRPO) to explicitly robustify the reasoning process against worst-case perturbations; at inference time, we augment the model with Randomized Smoothing to provide certified $L_2$-norm robustness guarantees. We evaluate SafeMed-R1 on the OmniMedVQA benchmark across eight medical imaging modalities comprising over 88,000 samples. Our experiments reveal that standard fine-tuned VLMs, despite achieving 95\% accuracy on clean inputs, collapse to approximately 25\% under PGD attacks. In contrast, SafeMed-R1 maintains 84.45\% accuracy under the same adversarial conditions, representing a 59 percentage point improvement in robustness. Furthermore, we demonstrate that models trained with explicit chain-of-thought reasoning exhibit superior adversarial robustness compared to instruction-only variants, suggesting a synergy between interpretability and security in medical AI systems.

