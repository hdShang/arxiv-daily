---
layout: default
title: ArtPerception: ASCII Art-based Jailbreak on LLMs with Recognition Pre-test
---

# ArtPerception: ASCII Art-based Jailbreak on LLMs with Recognition Pre-test

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.10281" target="_blank" class="toolbar-btn">arXiv: 2510.10281v1</a>
    <a href="https://arxiv.org/pdf/2510.10281.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10281v1" 
            onclick="toggleFavorite(this, '2510.10281v1', 'ArtPerception: ASCII Art-based Jailbreak on LLMs with Recognition Pre-test')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Guan-Yan Yang, Tzu-Yu Cheng, Ya-Wen Teng, Farn Wanga, Kuo-Hui Yeh

**分类**: cs.CR, cs.AI, cs.CL, cs.CV, cs.LG

**发布日期**: 2025-10-11

**备注**: 30 pages, 22 figures. This preprint has been accepted for publication in Elsevier JOURNAL OF NETWORK AND COMPUTER APPLICATIONS (JNCA)

**期刊**: Journal of Network and Computer Applications, Vol. 244, (2025) 104356

**DOI**: [10.1016/j.jnca.2025.104356](https://doi.org/10.1016/j.jnca.2025.104356)

---

## 💡 一句话要点

**ArtPerception：提出基于ASCII艺术的LLM越狱框架，通过识别预测试提升攻击效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `越狱攻击` `ASCII艺术` `安全对齐` `黑盒攻击`

## 📋 核心要点

1. 现有LLM安全对齐主要关注语义理解，忽略了非标准数据表示带来的安全风险，例如使用ASCII艺术进行攻击。
2. ArtPerception框架通过模型预测试确定ASCII艺术识别的最佳参数，从而实现高效的一次性越狱攻击。
3. 实验表明，ArtPerception在开源和商业LLM上均表现出卓越的越狱性能，并能有效对抗现有防御机制。

## 📝 摘要（中文）

大型语言模型（LLMs）集成到计算机应用中带来了变革性的能力，但也带来了重大的安全挑战。现有的安全对齐主要集中在语义解释上，使得LLMs容易受到使用非标准数据表示的攻击。本文介绍了一种新颖的黑盒越狱框架ArtPerception，它巧妙地利用ASCII艺术来绕过最先进（SOTA）LLMs的安全措施。与依赖迭代、蛮力攻击的先前方法不同，ArtPerception引入了一种系统的两阶段方法。第一阶段进行一次性的、模型特定的预测试，以经验性地确定ASCII艺术识别的最佳参数。第二阶段利用这些见解来发起高效的、一次性的恶意越狱攻击。我们提出了一种改进的Levenshtein距离（MLD）度量，用于更细致地评估LLM的识别能力。通过对四个SOTA开源LLMs的全面实验，我们展示了卓越的越狱性能。我们进一步验证了我们的框架的实际相关性，通过展示其成功转移到领先的商业模型，包括GPT-4o、Claude Sonnet 3.7和DeepSeek-V3，并通过对LLaMA Guard和Azure的内容过滤器等潜在防御措施进行严格的有效性分析。我们的研究结果表明，真正的LLM安全性需要防御多模态的解释空间，即使在纯文本输入中也是如此，并强调了战略性的、基于侦察的攻击的有效性。内容警告：本文包含潜在的有害和冒犯性的模型输出。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）容易受到非标准数据表示攻击的问题，特别是利用ASCII艺术绕过安全对齐机制。现有方法，如迭代式的蛮力攻击，效率低下且缺乏针对性。

**核心思路**：ArtPerception的核心思路是首先对目标LLM进行预测试，以了解其对ASCII艺术的识别能力，从而有针对性地生成能够绕过安全机制的恶意输入。这种“侦察”式的攻击方式避免了盲目的尝试，提高了攻击效率。

**技术框架**：ArtPerception框架包含两个主要阶段：
1. **预测试阶段**：针对特定LLM，通过一系列ASCII艺术样本进行测试，评估模型对不同参数（如字符大小、密度等）的识别能力。使用改进的Levenshtein距离（MLD）作为评估指标。
2. **攻击阶段**：基于预测试的结果，选择最优的ASCII艺术参数，生成恶意输入，诱导LLM产生有害或不当的输出。

**关键创新**：ArtPerception的关键创新在于其系统性的两阶段方法，特别是预测试阶段。通过预测试，该框架能够针对不同的LLM定制攻击策略，显著提高了攻击的成功率和效率。与以往的盲目攻击方法相比，ArtPerception更具针对性和智能化。

**关键设计**：
* **改进的Levenshtein距离（MLD）**：用于更准确地评估LLM对ASCII艺术的识别能力，考虑了字符之间的相似性和上下文关系。
* **预测试参数选择**：通过实验确定影响LLM识别能力的关键参数，如字符大小、密度、字体等，并选择最优参数组合。
* **一次性攻击**：基于预测试结果，生成一次性的恶意输入，避免了迭代攻击带来的时间和资源消耗。

## 📊 实验亮点

ArtPerception在四个SOTA开源LLM上展示了卓越的越狱性能，并成功转移到商业模型GPT-4o、Claude Sonnet 3.7和DeepSeek-V3。该框架能够有效对抗LLaMA Guard和Azure的内容过滤器等防御机制，证明了其在实际场景中的有效性和鲁棒性。

## 🎯 应用场景

ArtPerception的研究成果可应用于评估和提升LLM的安全性，特别是在对抗基于非标准数据表示的攻击方面。该研究有助于开发更强大的防御机制，防止LLM被恶意利用，保障其在各个领域的安全应用，例如智能客服、内容生成和代码辅助等。

## 📄 摘要（原文）

> The integration of Large Language Models (LLMs) into computer applications has introduced transformative capabilities but also significant security challenges. Existing safety alignments, which primarily focus on semantic interpretation, leave LLMs vulnerable to attacks that use non-standard data representations. This paper introduces ArtPerception, a novel black-box jailbreak framework that strategically leverages ASCII art to bypass the security measures of state-of-the-art (SOTA) LLMs. Unlike prior methods that rely on iterative, brute-force attacks, ArtPerception introduces a systematic, two-phase methodology. Phase 1 conducts a one-time, model-specific pre-test to empirically determine the optimal parameters for ASCII art recognition. Phase 2 leverages these insights to launch a highly efficient, one-shot malicious jailbreak attack. We propose a Modified Levenshtein Distance (MLD) metric for a more nuanced evaluation of an LLM's recognition capability. Through comprehensive experiments on four SOTA open-source LLMs, we demonstrate superior jailbreak performance. We further validate our framework's real-world relevance by showing its successful transferability to leading commercial models, including GPT-4o, Claude Sonnet 3.7, and DeepSeek-V3, and by conducting a rigorous effectiveness analysis against potential defenses such as LLaMA Guard and Azure's content filters. Our findings underscore that true LLM security requires defending against a multi-modal space of interpretations, even within text-only inputs, and highlight the effectiveness of strategic, reconnaissance-based attacks. Content Warning: This paper includes potentially harmful and offensive model outputs.

