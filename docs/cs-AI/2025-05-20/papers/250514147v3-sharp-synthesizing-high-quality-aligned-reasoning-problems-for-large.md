---
layout: default
title: SHARP: Synthesizing High-quality Aligned Reasoning Problems for Large Reasoning Models Reinforcement Learning
---

# SHARP: Synthesizing High-quality Aligned Reasoning Problems for Large Reasoning Models Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14147" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14147v3</a>
  <a href="https://arxiv.org/pdf/2505.14147.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14147v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14147v3', 'SHARP: Synthesizing High-quality Aligned Reasoning Problems for Large Reasoning Models Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiong Jun Wu, Zhenduo Zhang, ZuJie Wen, Zhiqiang Zhang, Wang Ren, Lei Shi, Cai Chen, Deng Zhao, Qing Wang, Xudong Han, Chengfu Tang, Dingnan Jin, Qing Cui, Jun Zhou

**分类**: cs.AI

**发布日期**: 2025-05-20 (更新: 2025-05-25)

---

## 💡 一句话要点

**提出SHARP以解决大规模推理模型训练中的问题生成挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理模型` `强化学习` `问题生成` `逻辑一致性` `教育技术` `STEM领域` `自对齐原则`

## 📋 核心要点

1. 现有方法在生成高质量、可验证的推理问题上存在不足，限制了大型推理模型的训练效果。
2. SHARP通过自对齐原则和三阶段框架，系统性地生成高质量的推理问题，确保逻辑一致性和可验证性。
3. 实验结果显示，SHARP增强的训练在复杂推理任务上显著提升了准确性，超越了现有方法的表现。

## 📝 摘要（中文）

在STEM领域，使用强化学习训练大型推理模型（LRMs）面临高质量、多样化和可验证问题集稀缺的挑战。现有合成方法，如思维链提示，常生成过于简化或不可验证的数据，限制了模型在复杂任务上的进展。为了解决这些问题，我们提出了SHARP，这是一种统一的方法，用于合成高质量对齐的推理问题，以支持LRMs的强化学习。SHARP包含一套自对齐原则，针对研究生和奥林匹克级别的难度，确保逻辑一致性和明确可验证的答案，并采用结构化的三阶段框架（对齐、实例化、推理），确保主题多样性和问题生成的细粒度控制。实验结果表明，SHARP增强的训练显著优于现有方法，提升了复杂推理的准确性，使LRM的表现更接近专家水平。

## 🔬 方法详解

**问题定义**：本论文旨在解决在STEM领域训练大型推理模型时，缺乏高质量和可验证问题集的问题。现有方法生成的数据往往过于简化或无法验证，限制了模型的学习能力。

**核心思路**：SHARP的核心思路是通过自对齐原则和结构化框架，系统性地生成高质量的推理问题，确保问题的逻辑一致性和答案的可验证性，从而提升模型的推理能力。

**技术框架**：SHARP的整体架构分为三个主要阶段：对齐（Alignment）、实例化（Instantiation）和推理（Inference）。在对齐阶段，定义问题的难度和逻辑结构；在实例化阶段，生成具体问题；在推理阶段，利用强化学习循环来验证和优化模型的推理过程。

**关键创新**：SHARP的主要创新在于其自对齐原则和三阶段框架的结合，确保生成的问题不仅具有挑战性，还能被有效验证。这一设计与现有方法的根本区别在于强调了问题的逻辑一致性和可验证性。

**关键设计**：在SHARP中，关键设计包括对问题难度的严格控制、逻辑一致性的保证，以及通过强化学习循环来优化模型的推理能力。这些设计确保了生成问题的高质量和多样性。

## 📊 实验亮点

实验结果表明，使用SHARP增强的训练方法在GPQA基准上显著提高了复杂推理的准确性，相较于现有方法提升幅度达到了未知的百分比，显示出SHARP在推动大型推理模型性能方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、科学研究和人工智能系统的训练，尤其是在需要复杂推理能力的STEM领域。SHARP的实施可以帮助教育工作者生成高质量的测试题，提升学生的学习效果，同时也为AI模型的训练提供了更为丰富和有效的数据支持，推动智能系统的进步。

## 📄 摘要（原文）

> Training large reasoning models (LRMs) with reinforcement learning in STEM domains is hindered by the scarcity of high-quality, diverse, and verifiable problem sets. Existing synthesis methods, such as Chain-of-Thought prompting, often generate oversimplified or uncheckable data, limiting model advancement on complex tasks. To address these challenges, we introduce SHARP, a unified approach to Synthesizing High-quality Aligned Reasoning Problems for LRMs reinforcement learning with verifiable rewards (RLVR). SHARP encompasses a strategic set of self-alignment principles -- targeting graduate and Olympiad-level difficulty, rigorous logical consistency, and unambiguous, verifiable answers -- and a structured three-phase framework (Alignment, Instantiation, Inference) that ensures thematic diversity and fine-grained control over problem generation. We implement SHARP by leveraging a state-of-the-art LRM to infer and verify challenging STEM questions, then employ a reinforcement learning loop to refine the model's reasoning through verifiable reward signals. Experiments on benchmarks such as GPQA demonstrate that SHARP-augmented training substantially outperforms existing methods, markedly improving complex reasoning accuracy and pushing LRM performance closer to expert-level proficiency. Our contributions include the SHARP strategy, framework design, end-to-end implementation, and experimental evaluation of its effectiveness in elevating LRM reasoning capabilities.

