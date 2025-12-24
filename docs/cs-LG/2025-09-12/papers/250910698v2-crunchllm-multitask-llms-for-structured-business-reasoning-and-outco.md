---
layout: default
title: "CrunchLLM: Multitask LLMs for Structured Business Reasoning and Outcome Prediction"
---

# CrunchLLM: Multitask LLMs for Structured Business Reasoning and Outcome Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10698" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10698v2</a>
  <a href="https://arxiv.org/pdf/2509.10698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10698v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10698v2', 'CrunchLLM: Multitask LLMs for Structured Business Reasoning and Outcome Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rabeya Tus Sadia, Qiang Cheng

**分类**: cs.LG, cs.CV

**发布日期**: 2025-09-12 (更新: 2025-10-11)

---

## 💡 一句话要点

**CrunchLLM：用于结构化商业推理和结果预测的多任务LLM**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `领域自适应` `创业预测` `结构化数据` `非结构化数据` `参数高效微调` `提示优化` `Crunchbase`

## 📋 核心要点

1. 现有方法难以有效利用Crunchbase等数据集中的结构化和非结构化异构数据来预测初创公司成功。
2. CrunchLLM通过融合结构化公司属性和非结构化文本叙述，并进行参数高效的微调和提示优化，实现领域自适应。
3. CrunchLLM在Crunchbase初创公司成功预测中准确率超过80%，显著优于传统分类器和基线LLM。

## 📝 摘要（中文）

预测初创公司的成功，定义为通过收购或首次公开募股（IPO）实现退出，是创业和创新研究中的一个关键问题。诸如Crunchbase之类的数据集提供了结构化信息（例如，融资轮次、行业、投资者网络）和非结构化文本（例如，公司描述），但有效地利用这种异构数据进行预测仍然具有挑战性。传统的机器学习方法通常仅依赖于结构化特征，并且准确性适中，而大型语言模型（LLM）提供了丰富的推理能力，但难以直接适应特定领域的业务数据。我们提出了	extbf{CrunchLLM}，一个用于初创公司成功预测的领域自适应LLM框架。CrunchLLM将结构化的公司属性与非结构化的文本叙述相结合，并应用参数高效的微调策略以及提示优化，以使基础模型专门用于创业数据。我们的方法在Crunchbase初创公司成功预测方面实现了超过80％的准确性，大大优于传统的分类器和基线LLM。除了预测性能之外，CrunchLLM还提供了可解释的推理轨迹，从而证明了其预测的合理性，从而增强了金融和政策决策者的透明度和可信赖性。这项工作表明，通过领域感知的微调和结构化-非结构化数据融合来调整LLM可以促进创业结果的预测建模。CrunchLLM为风险投资和创新政策中的数据驱动决策提供了一个方法论框架和一个实用工具。

## 🔬 方法详解

**问题定义**：论文旨在解决初创公司成功预测的问题，即预测一家初创公司是否能通过收购或IPO成功退出。现有方法，如传统机器学习模型，通常只利用结构化数据，忽略了非结构化文本信息，导致预测准确率不高。大型语言模型虽然具有强大的推理能力，但直接应用于特定领域的业务数据时效果不佳，缺乏领域知识。

**核心思路**：论文的核心思路是利用领域自适应的大型语言模型（LLM）来融合结构化和非结构化数据，从而提高初创公司成功预测的准确率。通过参数高效的微调和提示优化，使LLM能够更好地理解和利用创业领域的数据。

**技术框架**：CrunchLLM框架包含以下主要步骤：1) 数据准备：收集和处理Crunchbase数据集中的结构化公司属性（如融资轮次、行业）和非结构化文本叙述（如公司描述）。2) 模型选择：选择一个预训练的大型语言模型作为基础模型。3) 领域自适应微调：使用创业领域的数据对基础模型进行参数高效的微调，使其适应特定领域的知识。4) 提示优化：设计合适的提示，引导LLM进行推理和预测。5) 预测和解释：使用微调后的LLM进行初创公司成功预测，并提供可解释的推理轨迹。

**关键创新**：论文的关键创新在于将结构化和非结构化数据融合到LLM中，并采用参数高效的微调策略和提示优化，从而实现了领域自适应。与传统方法相比，CrunchLLM能够更好地利用异构数据，提高预测准确率，并提供可解释的推理过程。

**关键设计**：论文采用了参数高效的微调策略，例如LoRA或Adapter，以减少微调所需的计算资源。提示优化方面，设计了包含关键信息的提示模板，引导LLM进行推理。损失函数方面，可以使用交叉熵损失函数来训练模型，优化预测结果。具体的网络结构细节取决于所选择的基础LLM。

## 📊 实验亮点

CrunchLLM在Crunchbase初创公司成功预测任务中取得了显著的性能提升，准确率超过80%，大幅优于传统的机器学习分类器和基线LLM。这一结果表明，领域自适应的LLM在处理结构化和非结构化数据融合方面具有强大的潜力，能够为创业领域的预测建模提供更准确、更可靠的工具。

## 🎯 应用场景

CrunchLLM可应用于风险投资领域，帮助投资者评估初创公司的潜力，做出更明智的投资决策。此外，该模型还可用于创新政策制定，为政府机构提供数据支持，以促进创业和创新生态系统的发展。该研究的未来影响在于推动数据驱动的创业和创新决策，提高资源配置效率。

## 📄 摘要（原文）

> Predicting the success of start-up companies, defined as achieving an exit through acquisition or IPO, is a critical problem in entrepreneurship and innovation research. Datasets such as Crunchbase provide both structured information (e.g., funding rounds, industries, investor networks) and unstructured text (e.g., company descriptions), but effectively leveraging this heterogeneous data for prediction remains challenging. Traditional machine learning approaches often rely only on structured features and achieve moderate accuracy, while large language models (LLMs) offer rich reasoning abilities but struggle to adapt directly to domain-specific business data. We present \textbf{CrunchLLM}, a domain-adapted LLM framework for startup success prediction. CrunchLLM integrates structured company attributes with unstructured textual narratives and applies parameter-efficient fine-tuning strategies alongside prompt optimization to specialize foundation models for entrepreneurship data. Our approach achieves accuracy exceeding 80\% on Crunchbase startup success prediction, significantly outperforming traditional classifiers and baseline LLMs. Beyond predictive performance, CrunchLLM provides interpretable reasoning traces that justify its predictions, enhancing transparency and trustworthiness for financial and policy decision makers. This work demonstrates how adapting LLMs with domain-aware fine-tuning and structured--unstructured data fusion can advance predictive modeling of entrepreneurial outcomes. CrunchLLM contributes a methodological framework and a practical tool for data-driven decision making in venture capital and innovation policy.

