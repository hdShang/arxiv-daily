---
layout: default
title: "SBFA: Single Sneaky Bit Flip Attack to Break Large Language Models"
---

# SBFA: Single Sneaky Bit Flip Attack to Break Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21843" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21843v1</a>
  <a href="https://arxiv.org/pdf/2509.21843.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21843v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21843v1', 'SBFA: Single Sneaky Bit Flip Attack to Break Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingkai Guo, Chaitali Chakrabarti, Deliang Fan

**分类**: cs.CR, cs.CL, cs.LG

**发布日期**: 2025-09-26

**备注**: 10 pages, 4 figures, 5 tables, 2 equations. Topics: Bit-flip attacks, adversarial attacks, large language models (LLMs)

---

## 💡 一句话要点

**提出SBFA：单比特翻转攻击破解大语言模型，揭示严重安全隐患**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `比特翻转攻击` `大语言模型` `模型安全` `对抗攻击` `参数敏感性分析`

## 📋 核心要点

1. 现有比特翻转攻击（BFA）方法缺乏灵活性，通常仅针对整数或浮点模型，且在浮点模型中容易产生数值错误。
2. SBFA通过迭代搜索和ImpactScore指标，在保持参数分布良性的前提下，仅需单比特翻转即可破坏LLM性能。
3. 实验表明，SBFA在Qwen、LLaMA和Gemma等模型上，仅需单比特翻转即可将准确率降至随机水平以下，凸显安全风险。

## 📝 摘要（中文）

随着大语言模型（LLMs）的大规模在线部署，其模型完整性已成为一个紧迫的安全问题。先前的比特翻转攻击（BFAs）作为一种流行的AI权重内存故障注入技术，可以严重损害深度神经网络（DNNs）。即使只有几十个比特翻转，也能使准确率降低到随机猜测的水平。最近的研究将BFAs扩展到LLMs，并揭示尽管直觉上认为模块化和冗余会带来更好的鲁棒性，但少量的对抗性比特翻转也会导致LLMs的灾难性精度下降。然而，现有的BFA方法通常分别关注整数或浮点模型，限制了攻击的灵活性。此外，在浮点模型中，随机比特翻转通常会导致扰动参数达到极端值（例如，在指数位翻转），使其不隐蔽并导致数值运行时错误（例如，无效的张量值（NaN/Inf））。在这项工作中，我们首次提出了SBFA（Sneaky Bit-Flip Attack），它仅通过单个比特翻转就能使LLM性能崩溃，同时保持扰动值在良性的逐层权重分布范围内。这是通过迭代搜索和通过我们定义的参数敏感性指标ImpactScore进行排序来实现的，该指标结合了梯度敏感性和受良性逐层权重分布约束的扰动范围。还提出了一种新颖的轻量级SKIP搜索算法，以大大降低搜索复杂度，从而使SOTA LLM的SBFA搜索仅需花费数十分钟即可成功。在Qwen、LLaMA和Gemma模型中，仅通过单个比特翻转，SBFA就能成功地将BF16和INT8数据格式的MMLU和SST-2的准确率降低到随机水平以下。值得注意的是，在数十亿个参数中翻转单个比特揭示了SOTA LLM模型的严重安全问题。

## 🔬 方法详解

**问题定义**：论文旨在解决现有比特翻转攻击方法在攻击大语言模型时存在的局限性。现有方法要么只能处理特定数据类型的模型（整数或浮点数），要么在浮点数模型上进行攻击时容易导致参数值超出正常范围，引发数值错误，从而暴露攻击行为。这些问题限制了攻击的隐蔽性和有效性。

**核心思路**：论文的核心思路是通过寻找对模型性能影响最大，同时又不会显著改变参数分布的单个比特位进行翻转。这种“隐蔽”的攻击方式旨在避免触发模型的防御机制或导致数值计算错误。通过精心设计的参数敏感性指标和搜索算法，可以在大量参数中高效地找到这个关键比特。

**技术框架**：SBFA攻击框架主要包含以下几个阶段：1) **参数敏感性评估**：使用ImpactScore指标评估每个参数的敏感性，该指标结合了梯度敏感性和扰动范围约束。2) **候选比特位选择**：根据ImpactScore选择潜在的攻击目标比特位。3) **SKIP搜索算法**：利用轻量级的SKIP搜索算法，在候选比特位中高效地搜索最佳攻击比特。4) **攻击实施**：翻转选定的比特位，并评估模型性能。

**关键创新**：SBFA的关键创新在于：1) **单比特翻转攻击**：仅需翻转单个比特即可显著降低模型性能，提高了攻击的隐蔽性。2) **ImpactScore指标**：结合梯度敏感性和扰动范围约束，更准确地评估参数的敏感性。3) **SKIP搜索算法**：显著降低了搜索复杂度，使得在大型模型上进行攻击成为可能。

**关键设计**：ImpactScore指标的设计是关键。它综合考虑了梯度信息（反映参数对模型输出的影响）和参数扰动范围（确保翻转后的参数值仍在合理的分布范围内）。SKIP搜索算法通过跳过不重要的比特位，减少了搜索空间。此外，论文还针对BF16和INT8等不同数据格式进行了优化，确保攻击的有效性。

## 📊 实验亮点

实验结果表明，SBFA在Qwen、LLaMA和Gemma等SOTA LLM模型上，仅需翻转单个比特，就能将MMLU和SST-2数据集上的准确率降低到随机水平以下。例如，在某些模型上，准确率从原本的高水平直接降至10%以下，证明了SBFA攻击的有效性和LLM模型潜在的安全风险。

## 🎯 应用场景

SBFA的研究成果可应用于评估和提升大语言模型的安全性。通过模拟这种攻击，可以发现模型中的脆弱点，并开发相应的防御机制，例如异常检测、参数完整性校验等。此外，该研究也提醒开发者在模型部署时需要更加重视安全性，防止恶意攻击者利用类似的漏洞窃取信息或破坏服务。

## 📄 摘要（原文）

> Model integrity of Large language models (LLMs) has become a pressing security concern with their massive online deployment. Prior Bit-Flip Attacks (BFAs) -- a class of popular AI weight memory fault-injection techniques -- can severely compromise Deep Neural Networks (DNNs): as few as tens of bit flips can degrade accuracy toward random guessing. Recent studies extend BFAs to LLMs and reveal that, despite the intuition of better robustness from modularity and redundancy, only a handful of adversarial bit flips can also cause LLMs' catastrophic accuracy degradation. However, existing BFA methods typically focus on either integer or floating-point models separately, limiting attack flexibility. Moreover, in floating-point models, random bit flips often cause perturbed parameters to extreme values (e.g., flipping in exponent bit), making it not stealthy and leading to numerical runtime error (e.g., invalid tensor values (NaN/Inf)). In this work, for the first time, we propose SBFA (Sneaky Bit-Flip Attack), which collapses LLM performance with only one single bit flip while keeping perturbed values within benign layer-wise weight distribution. It is achieved through iterative searching and ranking through our defined parameter sensitivity metric, ImpactScore, which combines gradient sensitivity and perturbation range constrained by the benign layer-wise weight distribution. A novel lightweight SKIP searching algorithm is also proposed to greatly reduce searching complexity, which leads to successful SBFA searching taking only tens of minutes for SOTA LLMs. Across Qwen, LLaMA, and Gemma models, with only one single bit flip, SBFA successfully degrades accuracy to below random levels on MMLU and SST-2 in both BF16 and INT8 data formats. Remarkably, flipping a single bit out of billions of parameters reveals a severe security concern of SOTA LLM models.

