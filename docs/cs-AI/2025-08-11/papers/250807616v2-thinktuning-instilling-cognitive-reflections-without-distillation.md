---
layout: default
title: "ThinkTuning: Instilling Cognitive Reflections without Distillation"
---

# ThinkTuning: Instilling Cognitive Reflections without Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07616" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07616v2</a>
  <a href="https://arxiv.org/pdf/2508.07616.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07616v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07616v2', 'ThinkTuning: Instilling Cognitive Reflections without Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aswin RRV, Jacob Dineen, Divij Handa, Md Nayem Uddin, Mihir Parmar, Chitta Baral, Ben Zhou

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-08-11 (更新: 2025-08-21)

**备注**: EMNLP 2025 (Main Conference)

**🔗 代码/项目**: [GITHUB](https://github.com/3rdAT/ThinkTuning)

---

## 💡 一句话要点

**提出ThinkTuning以提升模型推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `思考型模型` `推理能力` `教师模型` `学生模型` `反馈机制` `强化学习` `GRPO` `互动训练`

## 📋 核心要点

1. 现有的强化学习方法无法真正赋予模型新的推理能力，仅能挖掘已有行为，导致推理能力的提升受限。
2. 本文提出的ThinkTuning方法通过教师模型的反馈来指导学生模型的思考过程，从而提升其推理能力。
3. 实验结果表明，ThinkTuning在多个基准测试中显著提升了模型的表现，平均提高3.85%。

## 📝 摘要（中文）

近年来，测试时扩展的进展促使了思考型大语言模型（LLMs）的出现，这些模型展现了自我反思行为和多步推理能力。尽管强化学习（RL）推动了这一自我改进的范式，但研究表明，RL并未真正赋予模型新的推理能力，而是仅仅挖掘了基础模型中已有的行为。因此，如何训练那些不具备思考行为的模型以发展这种能力成为一个重要问题。为此，本文提出了ThinkTuning，一种基于GRPO的互动训练方法，通过教师模型的指导增强学生模型的推理能力。实验结果显示，该方法在多个基准测试中平均提升了3.85%的性能，尤其在MATH-500、AIME和GPQA-Diamond上分别提升了2.08%、2.23%和3.99%。

## 🔬 方法详解

**问题定义**：本文旨在解决如何训练不具备思考行为的模型，使其能够发展出自我反思和多步推理能力。现有的强化学习方法未能有效实现这一目标，导致推理能力提升有限。

**核心思路**：ThinkTuning方法借鉴课堂教学中的反馈机制，通过教师模型的指导，帮助学生模型在尝试解答后获得纠正反馈，从而引导其思考并找到正确答案。

**技术框架**：该方法的整体架构包括教师模型和学生模型两个主要模块。教师模型负责提供问题和反馈，而学生模型则在教师的指导下进行尝试和学习。训练过程中，教师模型与学生模型的交互不断进行，以增强学生模型的推理能力。

**关键创新**：ThinkTuning的创新在于通过同等规模的教师模型提供隐性监督，显著改善学生模型的推理能力。这一方法与传统的强化学习方法不同，强调了反馈在学习过程中的重要性。

**关键设计**：在设计上，ThinkTuning采用了GRPO框架，设置了适当的损失函数以平衡教师反馈与学生模型的自主学习，确保反馈能够有效引导学生模型的思考过程。

## 📊 实验亮点

实验结果显示，ThinkTuning在多个基准测试中表现优异，平均提升了3.85%的性能。在MATH-500、AIME和GPQA-Diamond上，分别实现了2.08%、2.23%和3.99%的提升，相较于传统的vanilla-GRPO基线，展现了显著的优势。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和复杂问题求解等。通过提升模型的推理能力，ThinkTuning可以帮助开发更智能的学习工具，促进个性化学习和自主学习的实现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in test-time scaling have led to the emergence of thinking LLMs that exhibit self-reflective behaviors and multi-step reasoning. While RL drives this self-improvement paradigm, a recent study (Gandhi et al., 2025) shows that RL alone does not truly instill these new reasoning abilities - it merely draws out behaviors already present in the base models. This raises a question: How can we train the models that don't exhibit such thinking behavior to develop it in the first place? To this end, we propose ThinkTuning, a GRPO-based interactive training approach where we augment the rollouts of a student model with the guidance from a teacher model. A simple idea from classroom practice inspires our method: a teacher poses a problem, lets the student try an answer, then gives corrective feedback -- enough to point the mind in the right direction and then show the solution. Each piece of feedback reshapes the student's thoughts, leading them to arrive at the correct solution. Similarly, we find that this type of implicit supervision through feedback from a teacher model of the same size improves the reasoning capabilities of the student model. In particular, on average, our method shows a 3.85% improvement over zero-shot baselines across benchmarks, and on MATH-500, AIME and GPQA-Diamond it shows 2.08%, 2.23% and 3.99% improvements over the vanilla-GRPO baseline. Source code is available at https://github.com/3rdAT/ThinkTuning.

