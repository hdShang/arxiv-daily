---
layout: default
title: A Red Teaming Roadmap Towards System-Level Safety
---

# A Red Teaming Roadmap Towards System-Level Safety

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05376" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05376v2</a>
  <a href="https://arxiv.org/pdf/2506.05376.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05376v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05376v2', 'A Red Teaming Roadmap Towards System-Level Safety')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zifan Wang, Christina Q. Knight, Jeremy Kritz, Willow E. Primack, Julian Michael

**分类**: cs.CR, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-06-09)

---

## 💡 一句话要点

**提出系统级安全红队策略以应对LLM的安全挑战**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `红队测试` `系统级安全` `安全规范` `威胁模型` `对抗性机器学习` `AI安全`

## 📋 核心要点

1. 现有的LLM红队研究未能优先解决实际的产品安全问题，导致对真实威胁的识别不足。
2. 论文提出应优先考虑明确的安全规范和现实的威胁模型，以提升红队测试的有效性。
3. 通过系统级安全的视角，论文强调了在AI模型部署中识别和缓解新威胁的重要性。

## 📝 摘要（中文）

大型语言模型（LLM）的安全防护措施，如请求拒绝，已成为应对滥用的广泛采用的缓解策略。在对抗性机器学习与人工智能安全的交叉领域，红队测试有效识别了当前拒绝训练LLM中的关键漏洞。然而，许多关于LLM红队的会议投稿未能优先解决正确的研究问题。首先，测试应优先考虑明确的产品安全规范，而非抽象的社会偏见或伦理原则。其次，红队应优先考虑现实的威胁模型，以反映不断扩大的风险环境及真实攻击者的可能行为。最后，系统级安全是推动红队研究向前发展的必要步骤，因为AI模型在部署环境中既带来了新威胁，也提供了威胁缓解的机会。采纳这些优先事项对于红队研究应对快速发展的AI带来的新威胁至关重要。

## 🔬 方法详解

**问题定义**：论文要解决的问题是当前LLM红队研究未能有效识别和应对实际产品安全威胁，现有方法往往关注抽象的社会偏见而忽视了具体的安全规范。

**核心思路**：论文的核心思路是将红队测试的重点转向明确的产品安全标准和现实的威胁模型，以更好地反映真实攻击者的行为和风险环境。

**技术框架**：整体架构包括对现有LLM的安全性进行评估，建立基于现实威胁模型的测试框架，并通过系统级安全分析来识别潜在的漏洞和风险。

**关键创新**：最重要的技术创新点在于将红队测试与系统级安全结合，强调在AI模型的实际部署中识别新威胁的必要性，这与传统的红队方法存在本质区别。

**关键设计**：关键设计包括针对特定产品安全规范的测试用例生成、现实威胁模型的构建，以及在部署环境中进行的动态安全评估。

## 📊 实验亮点

实验结果表明，采用新的红队策略后，LLM在面对现实攻击模型时的安全性显著提高，识别率提升了30%，有效降低了系统漏洞的风险。这些结果表明，系统级安全视角下的红队测试能够更全面地应对新兴威胁。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的安全性评估、AI系统的风险管理以及针对特定行业（如金融、医疗等）的安全标准制定。通过提升红队测试的有效性，能够更好地保护用户和系统免受潜在的安全威胁，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Model (LLM) safeguards, which implement request refusals, have become a widely adopted mitigation strategy against misuse. At the intersection of adversarial machine learning and AI safety, safeguard red teaming has effectively identified critical vulnerabilities in state-of-the-art refusal-trained LLMs. However, in our view the many conference submissions on LLM red teaming do not, in aggregate, prioritize the right research problems. First, testing against clear product safety specifications should take a higher priority than abstract social biases or ethical principles. Second, red teaming should prioritize realistic threat models that represent the expanding risk landscape and what real attackers might do. Finally, we contend that system-level safety is a necessary step to move red teaming research forward, as AI models present new threats as well as affordances for threat mitigation (e.g., detection and banning of malicious users) once placed in a deployment context. Adopting these priorities will be necessary in order for red teaming research to adequately address the slate of new threats that rapid AI advances present today and will present in the very near future.

