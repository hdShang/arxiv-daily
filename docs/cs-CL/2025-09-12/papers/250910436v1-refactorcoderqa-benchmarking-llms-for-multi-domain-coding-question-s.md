---
layout: default
title: "RefactorCoderQA: Benchmarking LLMs for Multi-Domain Coding Question Solutions in Cloud and Edge Deployment"
---

# RefactorCoderQA: Benchmarking LLMs for Multi-Domain Coding Question Solutions in Cloud and Edge Deployment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10436" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10436v1</a>
  <a href="https://arxiv.org/pdf/2509.10436.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10436v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10436v1', 'RefactorCoderQA: Benchmarking LLMs for Multi-Domain Coding Question Solutions in Cloud and Edge Deployment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shadikur Rahman, Aroosa Hameed, Gautam Srivastava, Syed Muhammad Danish

**分类**: cs.CL

**发布日期**: 2025-09-12

**备注**: 12 pages, 5 figures, submitted to IEEE Transactions on Services Computing

---

## 💡 一句话要点

**提出RefactorCoderQA基准和云边协同架构，提升LLM在多领域代码问题解决能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码生成` `云边协同` `多智能体` `基准测试` `软件工程` `数据科学`

## 📋 核心要点

1. 现有代码生成基准覆盖范围有限，难以全面评估LLM在多领域复杂编码任务中的能力。
2. 提出云边协同架构，利用边缘轻量模型引导，云端强大模型求解，自动评估模型评价，提升代码生成质量。
3. 构建RefactorCoderQA基准，涵盖软件工程、数据科学等领域，实验表明RefactorCoder-MoE模型性能显著提升。

## 📝 摘要（中文）

为了优化大型语言模型（LLM）的推理和问题解决能力，我们提出了一种新颖的云边协同架构，该架构支持结构化的多智能体提示框架。该框架包含三个专门的组件：GuideLLM，一个部署在边缘的轻量级模型，用于提供方法论指导；SolverLLM，一个托管在云端的功能更强大的模型，负责生成代码解决方案；以及JudgeLLM，一个用于评估解决方案正确性和质量的自动评估器。为了评估和展示该架构在实际环境中的有效性，我们引入了RefactorCoderQA，这是一个综合基准，旨在评估和增强大型语言模型（LLM）在多领域编码任务中的性能。RefactorCoderQA 受到现有基准的局限性的推动，系统地涵盖了各种技术领域，包括软件工程、数据科学、机器学习和自然语言处理，使用了来自 Stack Overflow 的真实编码挑战。大量的实验表明，我们微调的模型 RefactorCoder-MoE 实现了最先进的性能，显著优于领先的开源和商业基线，总体准确率达到 76.84%。人工评估进一步验证了生成解决方案的可解释性、准确性和实际相关性。此外，我们还评估了吞吐量和延迟等系统级指标，以更深入地了解所提出架构的性能特征和权衡。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在多领域代码问题解决中的能力不足问题。现有方法或基准测试集通常覆盖范围有限，无法全面评估LLM在不同技术领域（如软件工程、数据科学、机器学习和自然语言处理）的复杂编码任务中的表现。此外，缺乏有效的架构来优化LLM的推理和问题解决能力，尤其是在资源受限的边缘设备上部署时。

**核心思路**：论文的核心思路是利用云边协同架构，结合多智能体提示框架，将问题解决过程分解为多个步骤，并分配给不同的模型。边缘设备上的轻量级模型（GuideLLM）负责提供方法论指导，云端的功能更强大的模型（SolverLLM）负责生成代码解决方案，最后由自动评估器（JudgeLLM）评估解决方案的正确性和质量。这种分工合作的方式可以充分利用云端和边缘设备的优势，提高代码生成效率和质量。

**技术框架**：整体架构包含三个主要模块：GuideLLM（边缘端，提供方法指导），SolverLLM（云端，生成代码解决方案），JudgeLLM（云端，评估解决方案）。流程如下：首先，GuideLLM接收编码问题，并生成解决该问题的方法论指导。然后，SolverLLM根据GuideLLM的指导生成代码解决方案。最后，JudgeLLM自动评估代码解决方案的正确性和质量，并提供反馈。

**关键创新**：关键创新点在于云边协同的多智能体提示框架，以及RefactorCoderQA基准测试集的构建。云边协同架构能够有效利用边缘设备的计算资源，降低延迟，同时利用云端的强大计算能力进行复杂的代码生成。RefactorCoderQA基准测试集涵盖了多个技术领域，能够更全面地评估LLM在不同领域的代码生成能力。

**关键设计**：GuideLLM是一个轻量级模型，旨在快速生成方法论指导，降低边缘设备的计算负担。SolverLLM是一个功能更强大的模型，例如MoE模型，旨在生成高质量的代码解决方案。JudgeLLM使用自动化测试和代码质量评估指标来评估解决方案的正确性和质量。RefactorCoder-MoE模型通过在RefactorCoderQA基准上进行微调，实现了最先进的性能。

## 📊 实验亮点

实验结果表明，提出的RefactorCoder-MoE模型在RefactorCoderQA基准测试集上取得了最先进的性能，总体准确率达到76.84%，显著优于领先的开源和商业基线。人工评估进一步验证了生成解决方案的可解释性、准确性和实际相关性。此外，系统级指标评估表明，该架构在吞吐量和延迟方面具有良好的性能。

## 🎯 应用场景

该研究成果可应用于自动化代码生成、智能编程助手、软件开发教育等领域。通过云边协同架构，可以为开发者提供更高效、更智能的代码生成服务，降低开发成本，提高开发效率。未来，该架构可以扩展到其他领域，例如机器人控制、智能制造等。

## 📄 摘要（原文）

> To optimize the reasoning and problem-solving capabilities of Large Language Models (LLMs), we propose a novel cloud-edge collaborative architecture that enables a structured, multi-agent prompting framework. This framework comprises three specialized components: GuideLLM, a lightweight model deployed at the edge to provide methodological guidance; SolverLLM, a more powerful model hosted in the cloud responsible for generating code solutions; and JudgeLLM, an automated evaluator for assessing solution correctness and quality. To evaluate and demonstrate the effectiveness of this architecture in realistic settings, we introduce RefactorCoderQA, a comprehensive benchmark designed to evaluate and enhance the performance of Large Language Models (LLMs) across multi-domain coding tasks. Motivated by the limitations of existing benchmarks, RefactorCoderQA systematically covers various technical domains, including Software Engineering, Data Science, Machine Learning, and Natural Language Processing, using authentic coding challenges from Stack Overflow. Extensive experiments reveal that our fine-tuned model, RefactorCoder-MoE, achieves state-of-the-art performance, significantly outperforming leading open-source and commercial baselines with an overall accuracy of 76.84%. Human evaluations further validate the interpretability, accuracy, and practical relevance of the generated solutions. In addition, we evaluate system-level metrics, such as throughput and latency, to gain deeper insights into the performance characteristics and trade-offs of the proposed architecture.

