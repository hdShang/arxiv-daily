---
layout: default
title: "Seed-Prover 1.5: Mastering Undergraduate-Level Theorem Proving via Learning from Experience"
---

# Seed-Prover 1.5: Mastering Undergraduate-Level Theorem Proving via Learning from Experience

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17260" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17260v1</a>
  <a href="https://arxiv.org/pdf/2512.17260.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17260v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17260v1', 'Seed-Prover 1.5: Mastering Undergraduate-Level Theorem Proving via Learning from Experience')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiangjie Chen, Wenxiang Chen, Jiacheng Du, Jinyi Hu, Zhicheng Jiang, Allan Jie, Xiaoran Jin, Xing Jin, Chenggang Li, Wenlei Shi, Zhihong Wang, Mingxuan Wang, Chenrui Wei, Shufa Wei, Huajian Xin, Fan Yang, Weihao Gao, Zheng Yuan, Tianyang Zhan, Zeyu Zheng, Tianxi Zhou, Thomas Hanwen Zhu

**分类**: cs.CL

**发布日期**: 2025-12-19

**备注**: 21 pages

---

## 💡 一句话要点

**Seed-Prover 1.5：通过经验学习掌握本科水平定理证明**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `形式化定理证明` `强化学习` `大型语言模型` `经验学习` `Lean` `自动化推理` `测试时缩放`

## 📋 核心要点

1. 现有方法利用LLM进行形式化定理证明时，面临计算成本高昂和难以处理本科以上难度问题等挑战。
2. Seed-Prover 1.5通过大规模强化学习，让模型与Lean等工具交互，持续积累经验，提升证明能力和效率。
3. 该模型结合测试时缩放（TTS）工作流程，有效连接自然语言和形式语言，并在多个基准测试中取得优异成绩。

## 📝 摘要（中文）

大型语言模型（LLMs）在生成严谨的数学证明方面取得了显著进展。然而，将LLMs应用于形式语言（如Lean）中的定理证明仍然具有挑战性且计算成本高昂，尤其是在解决本科及以上水平的问题时。本文提出了Seed-Prover 1.5，一个通过大规模agentic强化学习训练的形式定理证明模型，以及高效的测试时缩放（TTS）工作流程。通过与Lean和其他工具的广泛交互，该模型在强化学习过程中不断积累经验，从而显著提高了形式定理证明的能力和效率。此外，利用自然语言证明的最新进展，我们的TTS工作流程有效地弥合了自然语言和形式语言之间的差距。与最先进的方法相比，Seed-Prover 1.5以更小的计算预算实现了卓越的性能。它解决了88%的PutnamBench（本科水平）、80%的Fate-H（研究生水平）和33%的Fate-X（博士水平）问题。值得注意的是，使用我们的系统，我们在9小时内解决了Putnam 2025中的12个问题中的11个。我们的研究结果表明，由高质量的形式反馈驱动的经验学习扩展，为形式数学推理的未来提供了巨大的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决形式化定理证明领域中，现有大型语言模型在处理本科及以上难度问题时，计算成本高昂且证明能力不足的问题。现有方法难以有效利用形式化语言的精确性和结构化特点，导致在复杂定理证明任务中表现不佳。

**核心思路**：论文的核心思路是通过大规模的agentic强化学习，使模型能够与形式化证明环境（如Lean）进行交互，并从交互过程中积累经验。这种经验学习的方式能够让模型逐步掌握形式化证明的技巧和策略，从而提高证明的效率和成功率。同时，利用测试时缩放（TTS）工作流程，弥合自然语言和形式语言之间的差距，进一步提升模型的泛化能力。

**技术框架**：Seed-Prover 1.5的技术框架主要包括以下几个部分：1) 基于大型语言模型的agent，负责生成证明步骤；2) 形式化证明环境（如Lean），用于验证证明步骤的正确性并提供反馈；3) 强化学习算法，用于优化agent的策略，使其能够生成更有效的证明步骤；4) 测试时缩放（TTS）工作流程，用于将自然语言描述的问题转化为形式化语言，并对证明结果进行解释。整个流程通过不断迭代，使模型能够逐步提高形式化定理证明的能力。

**关键创新**：论文最重要的技术创新点在于将大规模agentic强化学习应用于形式化定理证明领域，并结合高效的测试时缩放（TTS）工作流程。这种方法能够充分利用形式化证明环境的反馈信息，使模型能够快速学习和适应不同的证明任务。与传统的基于规则或搜索的方法相比，Seed-Prover 1.5具有更强的泛化能力和更高的效率。

**关键设计**：论文的关键设计包括：1) 强化学习算法的选择，例如使用Proximal Policy Optimization (PPO) 或其他合适的算法；2) 奖励函数的设计，用于鼓励模型生成正确的证明步骤并避免错误的步骤；3) 网络结构的设计，例如使用Transformer或其他适合处理序列数据的结构；4) 测试时缩放（TTS）工作流程的具体实现，例如使用预训练的语言模型或专门设计的翻译模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17260v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17260v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17260v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Seed-Prover 1.5在PutnamBench（本科水平）上解决了88%的问题，在Fate-H（研究生水平）上解决了80%的问题，在Fate-X（博士水平）上解决了33%的问题。更值得关注的是，该系统在9小时内解决了Putnam 2025竞赛中的12个问题中的11个，展示了其强大的问题解决能力。

## 🎯 应用场景

该研究成果可应用于自动化定理证明、形式化验证、软件工程等领域。通过提高定理证明的效率和自动化程度，可以加速数学研究的进程，并提高软件和硬件系统的可靠性。未来，该技术有望应用于更广泛的领域，例如人工智能安全、智能合约验证等。

## 📄 摘要（原文）

> Large language models have recently made significant progress to generate rigorous mathematical proofs. In contrast, utilizing LLMs for theorem proving in formal languages (such as Lean) remains challenging and computationally expensive, particularly when addressing problems at the undergraduate level and beyond. In this work, we present \textbf{Seed-Prover 1.5}, a formal theorem-proving model trained via large-scale agentic reinforcement learning, alongside an efficient test-time scaling (TTS) workflow. Through extensive interactions with Lean and other tools, the model continuously accumulates experience during the RL process, substantially enhancing the capability and efficiency of formal theorem proving. Furthermore, leveraging recent advancements in natural language proving, our TTS workflow efficiently bridges the gap between natural and formal languages. Compared to state-of-the-art methods, Seed-Prover 1.5 achieves superior performance with a smaller compute budget. It solves \textbf{88\% of PutnamBench} (undergraduate-level), \textbf{80\% of Fate-H} (graduate-level), and \textbf{33\% of Fate-X} (PhD-level) problems. Notably, using our system, we solved \textbf{11 out of 12 problems} from Putnam 2025 within 9 hours. Our findings suggest that scaling learning from experience, driven by high-quality formal feedback, holds immense potential for the future of formal mathematical reasoning.

