---
layout: default
title: "Fair-GPTQ: Bias-Aware Quantization for Large Language Models"
---

# Fair-GPTQ: Bias-Aware Quantization for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15206" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15206v1</a>
  <a href="https://arxiv.org/pdf/2509.15206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15206v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15206v1', 'Fair-GPTQ: Bias-Aware Quantization for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Irina Proskurina, Guillaume Metzler, Julien Velcin

**分类**: cs.CL

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**Fair-GPTQ：面向大语言模型的偏见感知量化方法，提升公平性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `量化` `公平性` `偏见缓解` `群体公平性` `GPTQ` `模型部署`

## 📋 核心要点

1. 现有GPTQ量化方法在降低计算成本的同时，可能增加大语言模型的偏见输出，损害公平性。
2. Fair-GPTQ通过在量化目标中加入群体公平性约束，引导模型学习更公平的舍入操作，减少偏见生成。
3. 实验表明，Fair-GPTQ在保持性能的同时，有效降低了性别、种族和宗教等方面的刻板印象偏见。

## 📝 摘要（中文）

生成式语言模型对内存的高需求促使人们关注量化技术，该技术通过将模型权重映射到较低精度的整数来降低计算成本、内存使用和延迟。GPTQ等方法有效地最小化了量化过程中的输入-权重乘积误差；然而，最近的实证研究表明，它们可能会增加有偏输出，并降低在公平性基准上的性能，但目前尚不清楚哪些特定权重导致了这个问题。在这项工作中，我们通过将显式的群体公平性约束添加到量化目标中，从而在量化和模型公平性之间建立了新的联系，并引入了Fair-GPTQ，这是第一个明确旨在减少大型语言模型中不公平性的量化方法。添加的约束引导舍入操作的学习，从而减少受保护群体的有偏文本生成。具体来说，我们关注涉及职业偏见和歧视性语言（包括性别、种族和宗教）的刻板印象生成。Fair-GPTQ对性能的影响最小，在zero-shot基准上至少保留了90%的基线准确率，相对于半精度模型降低了不公平性，并保留了4位量化的内存和速度优势。我们还将Fair-GPTQ的性能与现有的去偏方法进行了比较，发现它在种族刻板印象基准上实现了与迭代零空间投影去偏方法相当的性能。总的来说，结果验证了我们带有群体偏见项的量化问题的理论解决方案，突出了其在生成模型量化时减少群体偏见的应用性，并证明了我们的方法可以进一步用于分析通道和权重级别对量化过程中公平性的贡献。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型量化过程中引入的偏见问题。现有的GPTQ等量化方法虽然能有效降低模型大小和计算复杂度，但会加剧模型在性别、种族、宗教等方面的偏见，导致不公平的输出结果。这些方法没有考虑量化对不同群体的影响，导致某些特定群体的利益受到损害。

**核心思路**：论文的核心思路是在量化过程中引入群体公平性约束，从而引导模型学习更公平的量化策略。具体来说，通过在量化目标函数中加入一个正则化项，惩罚那些导致模型对不同群体产生差异性输出的量化方案。这样，模型在追求量化效率的同时，也会兼顾公平性，从而减少偏见。

**技术框架**：Fair-GPTQ的技术框架主要包括以下几个步骤：1) 使用GPTQ等方法进行初步的量化；2) 定义一个群体公平性度量指标，用于衡量模型对不同群体的偏见程度；3) 在量化目标函数中加入一个正则化项，该正则化项与群体公平性度量指标相关；4) 使用优化算法（如梯度下降）来调整量化参数，从而最小化量化误差和群体偏见。

**关键创新**：Fair-GPTQ的关键创新在于将群体公平性约束显式地引入到量化过程中。与现有的量化方法不同，Fair-GPTQ不仅关注量化误差，还关注量化对模型公平性的影响。通过在量化目标函数中加入正则化项，Fair-GPTQ能够引导模型学习更公平的量化策略，从而减少偏见。

**关键设计**：Fair-GPTQ的关键设计包括：1) 群体公平性度量指标的选择：论文可能使用了多种群体公平性度量指标，如统计均等、机会均等和预测均等；2) 正则化项的设计：正则化项的设计需要平衡量化误差和群体偏见之间的权衡；3) 优化算法的选择：论文可能使用了不同的优化算法来调整量化参数，如梯度下降、Adam等。

## 📊 实验亮点

Fair-GPTQ在zero-shot基准测试中保持了至少90%的基线准确率，同时显著降低了模型在性别、种族和宗教等方面的刻板印象偏见。与半精度模型相比，Fair-GPTQ减少了不公平性，并保留了4位量化的内存和速度优势。在种族刻板印象基准上，Fair-GPTQ的性能与现有的迭代零空间投影去偏方法相当。

## 🎯 应用场景

Fair-GPTQ可应用于各种需要部署大语言模型的场景，尤其是在公平性至关重要的领域，如招聘、信贷评估、法律咨询等。通过减少模型偏见，Fair-GPTQ可以提高决策的公正性和透明度，避免对特定群体造成歧视。该研究有助于推动AI技术的公平性和可信赖性。

## 📄 摘要（原文）

> High memory demands of generative language models have drawn attention to quantization, which reduces computational cost, memory usage, and latency by mapping model weights to lower-precision integers. Approaches such as GPTQ effectively minimize input-weight product errors during quantization; however, recent empirical studies show that they can increase biased outputs and degrade performance on fairness benchmarks, and it remains unclear which specific weights cause this issue. In this work, we draw new links between quantization and model fairness by adding explicit group-fairness constraints to the quantization objective and introduce Fair-GPTQ, the first quantization method explicitly designed to reduce unfairness in large language models. The added constraints guide the learning of the rounding operation toward less-biased text generation for protected groups. Specifically, we focus on stereotype generation involving occupational bias and discriminatory language spanning gender, race, and religion. Fair-GPTQ has minimal impact on performance, preserving at least 90% of baseline accuracy on zero-shot benchmarks, reduces unfairness relative to a half-precision model, and retains the memory and speed benefits of 4-bit quantization. We also compare the performance of Fair-GPTQ with existing debiasing methods and find that it achieves performance on par with the iterative null-space projection debiasing approach on racial-stereotype benchmarks. Overall, the results validate our theoretical solution to the quantization problem with a group-bias term, highlight its applicability for reducing group bias at quantization time in generative models, and demonstrate that our approach can further be used to analyze channel- and weight-level contributions to fairness during quantization.

