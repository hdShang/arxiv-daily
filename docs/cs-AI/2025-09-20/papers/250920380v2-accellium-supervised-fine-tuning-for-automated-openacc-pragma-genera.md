---
layout: default
title: "ACCeLLiuM: Supervised Fine-Tuning for Automated OpenACC Pragma Generation"
---

# ACCeLLiuM: Supervised Fine-Tuning for Automated OpenACC Pragma Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20380" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20380v2</a>
  <a href="https://arxiv.org/pdf/2509.20380.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20380v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20380v2', 'ACCeLLiuM: Supervised Fine-Tuning for Automated OpenACC Pragma Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Samyak Jhaveri, Vanessa Klotzmann, Crista Lopes

**分类**: cs.SE, cs.AI, cs.PL

**发布日期**: 2025-09-20 (更新: 2025-09-26)

---

## 💡 一句话要点

**ACCeLLiuM：用于自动生成OpenACC编译指导语句的监督式微调方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `OpenACC` `GPU编程` `编译指导语句生成` `大型语言模型` `监督式微调`

## 📋 核心要点

1. GPU编程复杂性高，OpenACC等指令式编程虽简化了流程，但仍需专业知识。
2. ACCeLLiuM通过微调LLM，使其能为数据并行循环自动生成OpenACC编译指导语句。
3. 实验表明，微调后的LLM在生成正确OpenACC编译指导语句方面显著优于基础LLM。

## 📝 摘要（中文）

随着GPU日益普及，其硬件和并行编程框架的复杂性也随之增加。基于指令的并行编程标准（如OpenACC）通过抽象底层复杂性，在一定程度上简化了GPU编程，但有效使用这些指令仍然需要相当多的专业知识。我们介绍了ACCeLLiuM，这是两个开放权重的大型语言模型，专门针对为数据并行循环生成专家级OpenACC指令进行微调，以及用于训练它们的监督式微调数据集。ACCeLLiuM SFT数据集包含从公共GitHub C/C++存储库中挖掘的4,033个OpenACC pragma-loop对，其中3,223对用于训练，810对用于测试。实验评估表明，基础LLM和我们微调版本在生成正确的OpenACC编译指导语句方面存在显著的性能差距。在保留的测试集上，基础LLM无法始终如一地生成有效的编译指导语句，而基于ACCeLLiuM数据集微调的LLM能够为87%的数据并行循环生成具有正确指令类型的有效编译指导语句，并在50%的情况下生成精确的编译指导语句（包括指令、子句、子句顺序和子句变量）。即使不完全匹配，生成的编译指导语句也经常以不同于ground-truth标签的顺序包含正确的子句，或者包含额外的子句，从而可以更好地控制并行执行、数据移动和并发性，从而提供超出严格字符串匹配的实际价值。通过公开发布代码、模型和数据集ACCeLLiuM，我们希望为LLM驱动的OpenACC编译指导语句生成建立一个可复现的基准，并降低自动将串行编写的程序卸载到GPU的门槛。

## 🔬 方法详解

**问题定义**：论文旨在解决GPU编程中OpenACC编译指导语句生成需要专业知识的问题。现有方法依赖人工编写，效率低且易出错，难以充分利用GPU的并行计算能力。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）强大的代码理解和生成能力，通过监督式微调，使LLM能够自动生成高质量的OpenACC编译指导语句。这样可以降低GPU编程的门槛，提高开发效率。

**技术框架**：ACCeLLiuM的技术框架主要包括以下几个部分：1) 构建OpenACC pragma-loop对的监督式微调数据集；2) 选择合适的LLM作为基础模型；3) 使用监督式学习方法，在构建的数据集上对LLM进行微调；4) 对微调后的LLM进行评估，验证其生成OpenACC编译指导语句的性能。

**关键创新**：论文的关键创新在于：1) 构建了一个高质量的OpenACC pragma-loop对数据集，为LLM的微调提供了数据基础；2) 提出了一种基于监督式微调的OpenACC编译指导语句自动生成方法，显著提高了生成编译指导语句的准确性和效率；3) 公开了代码、模型和数据集，为该领域的研究提供了可复现的基准。

**关键设计**：ACCeLLiuM的关键设计包括：1) 数据集的构建：从GitHub等公共代码仓库中挖掘C/C++代码，提取数据并行循环和对应的OpenACC编译指导语句，并进行清洗和预处理；2) 模型选择：选择了具有较强代码理解和生成能力的LLM作为基础模型（具体模型未知）；3) 微调策略：采用监督式学习方法，使用交叉熵损失函数等（具体损失函数未知）对LLM进行微调，优化模型生成OpenACC编译指导语句的准确性。

## 📊 实验亮点

实验结果表明，在保留的测试集上，基于ACCeLLiuM数据集微调的LLM能够为87%的数据并行循环生成具有正确指令类型的有效编译指导语句，并在50%的情况下生成精确的编译指导语句。这表明ACCeLLiuM在自动生成OpenACC编译指导语句方面具有显著的性能优势。

## 🎯 应用场景

ACCeLLiuM可应用于高性能计算、科学计算、图像处理等领域，通过自动生成OpenACC编译指导语句，简化GPU编程，加速应用程序的开发和优化。该研究有助于降低GPU编程门槛，促进GPU在更多领域的应用，并推动并行计算技术的发展。

## 📄 摘要（原文）

> The increasing ubiquity of GPUs is accompanied by the increasing complexity of their hardware and parallel programming frameworks. Directive-based parallel programming standards like OpenACC simplify GPU programming to some extent by abstracting away low-level complexities, but a fair amount of expertise is still required in order to use those directives effectively.
>   We introduce ACCeLLiuM, two open weights Large Language Models specifically fine-tuned for generating expert OpenACC directives for data-parallel loops, along with the supervised fine-tuning dataset that was used to train them. The ACCeLLiuM SFT dataset contains 4,033 OpenACC pragma-loop pairs mined from public GitHub C/C++ repositories, with 3,223 pairs for training and 810 for testing. Experimental evaluations show a pronounced performance gap in generating correct OpenACC pragmas between base LLMs and our fine-tuned versions. On the held-out test set, base LLMs fail to consistently generate valid pragmas, whereas LLMs fine-tuned on the ACCeLLiuM dataset generate valid pragmas with the correct directive type for $87\%$ of the data-parallel loops, and exact pragmas--including directives, clauses, clause order, and clause variables--for $50\%$ of the cases. Even when not exact, generated pragmas frequently incorporate the correct clauses in a different order than the ground-truth label, or include additional clauses that enable finer control over parallel execution, data movement, and concurrency, offering practical value beyond strict string-matching. By publicly releasing the code, models, and dataset as ACCeLLiuM we hope to establish a reproducible benchmark for LLM-powered OpenACC pragma generation, and lower the barrier to automated GPU offloading of serially written programs.

