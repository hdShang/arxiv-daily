---
layout: default
title: AI Security Beyond Core Domains: Resume Screening as a Case Study of Adversarial Vulnerabilities in Specialized LLM Applications
---

# AI Security Beyond Core Domains: Resume Screening as a Case Study of Adversarial Vulnerabilities in Specialized LLM Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20164" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20164v1</a>
  <a href="https://arxiv.org/pdf/2512.20164.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20164v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20164v1', 'AI Security Beyond Core Domains: Resume Screening as a Case Study of Adversarial Vulnerabilities in Specialized LLM Applications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Honglin Mu, Jinghao Liu, Kaiyang Wan, Rui Xing, Xiuying Chen, Timothy Baldwin, Wanxiang Che

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**揭示LLM在简历筛选等专业应用中对抗性漏洞，并提出有效防御方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `对抗性攻击` `简历筛选` `安全漏洞` `LoRA适配`

## 📋 核心要点

1. 现有LLM在简历筛选等专业领域应用中，缺乏针对对抗性指令攻击的有效防御机制，存在安全隐患。
2. 论文提出FIDS（通过分离进行外部指令检测）方法，利用LoRA适配增强模型对对抗性指令的识别能力。
3. 实验表明，FIDS及与prompt-based防御结合的方法，能有效降低攻击成功率，且训练时防御优于推理时缓解。

## 📝 摘要（中文）

大型语言模型（LLM）在文本理解和生成方面表现出色，使其成为代码审查和内容审核等自动化任务的理想选择。然而，我们的研究发现了一个漏洞：LLM容易受到隐藏在输入数据（如简历或代码）中的“对抗性指令”的操纵，导致它们偏离预期的任务。值得注意的是，虽然针对代码审查等成熟领域可能存在防御机制，但在简历筛选和同行评审等其他常见应用中，这些防御机制往往缺失。本文引入了一个基准来评估简历筛选中的这种漏洞，揭示了某些攻击类型的成功率超过80%。我们评估了两种防御机制：基于提示的防御实现了10.1%的攻击减少，但误拒率增加了12.5%，而我们提出的使用LoRA适配的FIDS（通过分离进行外部指令检测）实现了15.4%的攻击减少，误拒率增加了10.4%。组合方法提供了26.3%的攻击减少，表明训练时防御在安全性和效用保持方面均优于推理时缓解。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM在简历筛选等专业应用中，容易受到对抗性指令攻击的问题。现有方法，特别是针对代码审查等成熟领域的防御机制，无法直接应用于这些专业领域，导致LLM在处理简历等数据时容易被恶意指令操纵，偏离预定目标。

**核心思路**：论文的核心思路是通过训练时防御，增强LLM对对抗性指令的识别和抵抗能力。具体而言，论文提出了FIDS（Foreign Instruction Detection through Separation）方法，旨在将模型对正常指令和对抗性指令的响应分离，从而更容易检测和过滤对抗性指令。

**技术框架**：整体框架包含两个主要阶段：攻击阶段和防御阶段。在攻击阶段，研究者构建对抗性指令并将其嵌入到简历中，以评估LLM的脆弱性。在防御阶段，研究者评估了prompt-based防御和FIDS两种方法。FIDS使用LoRA（Low-Rank Adaptation）技术，在预训练的LLM基础上进行微调，以区分正常指令和对抗性指令。

**关键创新**：最重要的技术创新点在于FIDS方法，它通过LoRA适配，在训练过程中显式地学习区分正常指令和对抗性指令，从而提高了模型对对抗性攻击的鲁棒性。与传统的推理时防御方法相比，FIDS在训练时就融入了防御机制，能够更有效地抵御对抗性攻击。

**关键设计**：FIDS的关键设计在于使用LoRA适配器。LoRA通过引入低秩矩阵来更新预训练模型的权重，从而在微调过程中减少了计算量和内存消耗。在FIDS中，LoRA被用于学习区分正常指令和对抗性指令的特征表示。此外，论文还探索了prompt-based防御，通过修改输入提示来引导LLM忽略对抗性指令。损失函数的设计可能涉及对比学习或交叉熵损失，以鼓励模型区分正常和对抗性指令的表示。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20164v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20164v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20164v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，某些攻击类型的成功率超过80%，凸显了LLM在简历筛选等专业应用中的安全风险。FIDS方法实现了15.4%的攻击减少，误拒率增加了10.4%。结合prompt-based防御，攻击减少率达到26.3%，表明训练时防御策略优于推理时缓解策略。这些数据验证了FIDS的有效性，并为LLM安全防御提供了新的思路。

## 🎯 应用场景

该研究成果可应用于各种基于LLM的自动化任务，如招聘领域的简历筛选、学术领域的论文评审、以及内容审核等。通过提升LLM对抗恶意指令攻击的鲁棒性，可以提高自动化系统的安全性和可靠性，减少人工干预，提高工作效率。未来，该研究可以扩展到其他专业领域，并与其他防御技术相结合，构建更强大的安全防护体系。

## 📄 摘要（原文）

> Large Language Models (LLMs) excel at text comprehension and generation, making them ideal for automated tasks like code review and content moderation. However, our research identifies a vulnerability: LLMs can be manipulated by "adversarial instructions" hidden in input data, such as resumes or code, causing them to deviate from their intended task. Notably, while defenses may exist for mature domains such as code review, they are often absent in other common applications such as resume screening and peer review. This paper introduces a benchmark to assess this vulnerability in resume screening, revealing attack success rates exceeding 80% for certain attack types. We evaluate two defense mechanisms: prompt-based defenses achieve 10.1% attack reduction with 12.5% false rejection increase, while our proposed FIDS (Foreign Instruction Detection through Separation) using LoRA adaptation achieves 15.4% attack reduction with 10.4% false rejection increase. The combined approach provides 26.3% attack reduction, demonstrating that training-time defenses outperform inference-time mitigations in both security and utility preservation.

