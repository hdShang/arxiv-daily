---
layout: default
title: "ARIAL: An Agentic Framework for Document VQA with Precise Answer Localization"
---

# ARIAL: An Agentic Framework for Document VQA with Precise Answer Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18192" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18192v2</a>
  <a href="https://arxiv.org/pdf/2511.18192.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18192v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18192v2', 'ARIAL: An Agentic Framework for Document VQA with Precise Answer Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahmad Mohammadshirazi, Pinaki Prasad Guha Neogi, Dheeraj Kulshrestha, Rajiv Ramnath

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-22 (更新: 2025-11-28)

---

## 💡 一句话要点

**提出ARIAL框架，通过Agentic方式实现文档VQA的精确答案定位与抽取。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `文档视觉问答` `Agentic框架` `答案定位` `LLM规划代理` `模块化设计`

## 📋 核心要点

1. 现有文档VQA系统在文本准确率和空间定位精度之间存在trade-off，难以同时保证两者。
2. ARIAL框架利用LLM作为规划代理，协调OCR、检索、答案生成和定位等模块，实现精确答案抽取和定位。
3. 实验表明，ARIAL在DocVQA等数据集上超越现有SOTA方法，在文本准确率和空间精度上均有显著提升。

## 📝 摘要（中文）

文档视觉问答(VQA)不仅要求模型提取准确的文本答案，还需要在文档图像中精确定位答案，这对于高风险应用中的可解释性至关重要。然而，现有系统在实现强大的文本准确性的同时，产生了不可靠的空间定位，或者牺牲性能来换取可解释性。我们提出了ARIAL（Agentic Reasoning for Interpretable Answer Localization），一个模块化框架，通过基于LLM的规划代理来协调专门的工具，以实现精确的答案提取和可靠的空间定位。ARIAL将文档VQA分解为结构化的子任务：使用TrOCR进行基于OCR的文本提取，使用语义搜索进行检索增强的上下文选择，通过微调的Gemma 3-27B模型生成答案，以及通过文本到区域对齐进行显式的边界框定位。这种模块化架构产生了透明的推理轨迹，从而实现了工具级别的可审计性和独立的组件优化。我们在四个基准数据集（DocVQA、FUNSD、CORD和SROIE）上评估了ARIAL，使用了文本准确性（ANLS）和空间精度（IoU 0.50到0.95的mAP）。ARIAL在所有数据集上都取得了最先进的结果：在DocVQA上达到88.7 ANLS和50.1 mAP，在FUNSD上达到90.0 ANLS和50.3 mAP，在CORD上达到85.5 ANLS和60.2 mAP，在SROIE上达到93.1 ANLS，超过了之前最好的方法（DLaVA），在DocVQA上提升了+2.8 ANLS和+3.9 mAP。我们的工作表明，专门工具的Agentic编排可以同时提高性能和可解释性，为可信赖、可解释的文档AI系统提供了一条途径。

## 🔬 方法详解

**问题定义**：文档视觉问答（Document VQA）任务旨在根据给定的文档图像和问题，提取准确的文本答案，并精确定位答案在图像中的位置。现有方法要么侧重于提高文本答案的准确性，而忽略了空间定位的可靠性；要么为了提高可解释性而牺牲了整体性能。因此，如何同时实现高准确率的答案提取和高精度的空间定位是当前文档VQA面临的主要挑战。

**核心思路**：ARIAL的核心思路是将文档VQA任务分解为一系列结构化的子任务，并利用大型语言模型（LLM）作为规划代理，协调不同的专业工具来完成这些子任务。通过这种模块化的Agentic方式，可以充分利用每个工具的优势，并实现透明的推理过程，从而提高整体性能和可解释性。

**技术框架**：ARIAL框架包含以下主要模块：1) **OCR文本提取**：使用TrOCR从文档图像中提取文本信息。2) **检索增强的上下文选择**：利用语义搜索技术，从提取的文本中选择与问题相关的上下文信息。3) **答案生成**：使用微调的Gemma 3-27B模型，根据问题和上下文信息生成答案。4) **边界框定位**：通过文本到区域的对齐，将生成的答案定位到文档图像中的具体位置。LLM作为规划代理，负责协调这些模块的执行顺序和参数设置。

**关键创新**：ARIAL的关键创新在于其Agentic框架的设计，它将文档VQA任务分解为多个可管理的子任务，并利用LLM作为规划代理来协调这些子任务的执行。这种模块化的设计不仅提高了整体性能，还增强了模型的可解释性和可审计性。与现有方法相比，ARIAL能够更有效地利用各种专业工具的优势，并实现更精确的答案定位。

**关键设计**：ARIAL框架的关键设计包括：1) 使用TrOCR进行OCR文本提取，确保文本信息的准确性。2) 利用语义搜索技术进行上下文选择，提高答案生成的质量。3) 使用微调的Gemma 3-27B模型生成答案，充分利用LLM的强大能力。4) 通过文本到区域的对齐进行边界框定位，实现精确的空间定位。此外，LLM规划代理的设计也至关重要，它需要能够有效地协调各个模块的执行，并根据任务需求进行动态调整。

## 📊 实验亮点

ARIAL在DocVQA、FUNSD、CORD和SROIE四个基准数据集上取得了SOTA结果。在DocVQA数据集上，ARIAL的ANLS指标达到88.7，mAP指标达到50.1，相比之前的最佳方法DLaVA，分别提升了+2.8 ANLS和+3.9 mAP。这些结果表明，ARIAL框架在文本准确率和空间精度上均具有显著优势。

## 🎯 应用场景

ARIAL框架具有广泛的应用前景，例如在金融、法律、医疗等领域，可以用于自动处理文档、提取关键信息、回答用户提问等。该研究有助于提升文档AI系统的可信度和可解释性，使其能够更好地服务于高风险应用场景，并为未来的文档智能研究提供新的思路。

## 📄 摘要（原文）

> Document Visual Question Answering (VQA) requires models to not only extract accurate textual answers but also precisely localize them within document images, a capability critical for interpretability in high-stakes applications. However, existing systems achieve strong textual accuracy while producing unreliable spatial grounding, or sacrifice performance for interpretability. We present ARIAL (Agentic Reasoning for Interpretable Answer Localization), a modular framework that orchestrates specialized tools through an LLM-based planning agent to achieve both precise answer extraction and reliable spatial grounding. ARIAL decomposes Document VQA into structured subtasks: OCR-based text extraction with TrOCR, retrieval-augmented context selection using semantic search, answer generation via a fine-tuned Gemma 3-27B model, and explicit bounding-box localization through text-to-region alignment. This modular architecture produces transparent reasoning traces, enabling tool-level auditability and independent component optimization. We evaluate ARIAL on four benchmarks (DocVQA, FUNSD, CORD, and SROIE) using both textual accuracy (ANLS) and spatial precision (mAP at IoU 0.50 to 0.95). ARIAL achieves state-of-the-art results across all datasets: 88.7 ANLS and 50.1 mAP on DocVQA, 90.0 ANLS and 50.3 mAP on FUNSD, 85.5 ANLS and 60.2 mAP on CORD, and 93.1 ANLS on SROIE, surpassing the previous best method (DLaVA) by +2.8 ANLS and +3.9 mAP on DocVQA. Our work demonstrates how agentic orchestration of specialized tools can simultaneously improve performance and interpretability, providing a pathway toward trustworthy, explainable document AI systems.

