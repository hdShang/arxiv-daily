---
layout: default
title: AnySleep: a channel-agnostic deep learning system for high-resolution sleep staging in multi-center cohorts
---

# AnySleep: a channel-agnostic deep learning system for high-resolution sleep staging in multi-center cohorts

**arXiv**: [2512.14461v1](https://arxiv.org/abs/2512.14461) | [PDF](https://arxiv.org/pdf/2512.14461.pdf)

**作者**: Niklas Grieger, Jannik Raskob, Siamak Mehrkanoon, Stephan Bialonski

**分类**: cs.LG, eess.SP, q-bio.QM

**发布日期**: 2025-12-16

**备注**: 18 pages, 6 figures, 2 tables

---

## 💡 一句话要点

**提出AnySleep深度学习系统，以解决多中心睡眠研究中电极设置异质性和时间分辨率限制的问题。**

**关键词**: `睡眠分期` `深度学习` `多中心研究` `脑电图分析` `时间分辨率` `生物标志物发现` `通道无关模型` `睡眠障碍诊断`

## 📋 核心要点

1. 核心问题：传统睡眠分期依赖手动评分，耗时且在多中心研究中因电极设置、导联方式和受试者差异而难以协调，限制了短时间尺度生物标志物的发现。
2. 方法要点：提出AnySleep深度神经网络，利用任意EEG或EOG数据，支持可调时间分辨率，通过大规模多中心数据训练实现跨站点稳健泛化。
3. 实验或效果：模型在30秒周期达到SOTA性能，在子30秒尺度捕捉短时觉醒，提升年龄、性别和睡眠呼吸暂停等特征的预测准确性。

## 📝 摘要（中文）

睡眠对健康至关重要，但研究其动态需要手动睡眠分期，这在睡眠研究和临床护理中是一项劳动密集型步骤。传统上，多中心多导睡眠图（PSG）记录通常以30秒为周期进行评分，这更多是出于实用而非生理原因，且电极数量、导联方式和受试者特征差异显著。这些限制给开展协调的多中心睡眠研究以及在更短时间尺度上发现新颖、稳健的生物标志物带来了挑战。本文提出AnySleep，一种深度神经网络模型，可利用任何脑电图（EEG）或眼电图（EOG）数据，以可调的时间分辨率进行睡眠分期。我们在来自21个数据集的超过19,000个夜间记录上训练和验证了该模型，涵盖近200,000小时的EEG和EOG数据，以促进跨站点的稳健泛化。该模型达到了最先进的性能，在30秒周期上超越或等同于现有基线。随着提供更多通道，性能有所提升，但在EOG缺失或仅使用EOG或单个EEG导联（额叶、中央或枕叶）时仍保持强劲。在低于30秒的时间尺度上，模型能捕捉与觉醒一致的短暂清醒侵入，并相对于标准的30秒评分，改善了生理特征（年龄、性别）和病理生理状况（睡眠呼吸暂停）的预测。我们公开提供该模型，以促进具有异质电极设置的大规模研究，并加速睡眠中新生物标志物的发现。

## 🔬 方法详解

AnySleep是一个深度神经网络模型，整体框架基于深度学习技术，设计为通道无关，可处理任意EEG或EOG输入数据。关键技术创新点包括：支持可调时间分辨率（如低于30秒），以捕捉更精细的睡眠动态；通过大规模多中心数据集（超过19,000个记录）训练，增强模型对异质电极设置和站点差异的泛化能力。与现有方法的主要区别在于：传统方法通常固定于30秒周期且依赖特定电极配置，而AnySleep灵活适应不同通道组合（如仅EOG或单EEG导联），并优化了短时间尺度分析，从而克服了多中心研究中的协调挑战。

## 📊 实验亮点

模型在30秒周期达到最先进性能，超越或等于基线；在子30秒时间尺度，能有效捕捉短时觉醒，提升年龄、性别和睡眠呼吸暂停的预测准确性；即使仅使用EOG或单EEG导联，性能仍保持强劲，展示了卓越的泛化能力。

## 🎯 应用场景

该研究可应用于多中心睡眠研究、临床睡眠监测和生物标志物发现。实际价值在于：促进大规模异质电极设置下的协调研究，加速新睡眠生物标志物的识别，并支持个性化睡眠健康评估，如改善睡眠障碍（如睡眠呼吸暂停）的诊断和监测。

## 📄 摘要（原文）

> Sleep is essential for good health throughout our lives, yet studying its dynamics requires manual sleep staging, a labor-intensive step in sleep research and clinical care. Across centers, polysomnography (PSG) recordings are traditionally scored in 30-s epochs for pragmatic, not physiological, reasons and can vary considerably in electrode count, montage, and subject characteristics. These constraints present challenges in conducting harmonized multi-center sleep studies and discovering novel, robust biomarkers on shorter timescales. Here, we present AnySleep, a deep neural network model that uses any electroencephalography (EEG) or electrooculography (EOG) data to score sleep at adjustable temporal resolutions. We trained and validated the model on over 19,000 overnight recordings from 21 datasets collected across multiple clinics, spanning nearly 200,000 hours of EEG and EOG data, to promote robust generalization across sites. The model attains state-of-the-art performance and surpasses or equals established baselines at 30-s epochs. Performance improves as more channels are provided, yet remains strong when EOG is absent or when only EOG or single EEG derivations (frontal, central, or occipital) are available. On sub-30-s timescales, the model captures short wake intrusions consistent with arousals and improves prediction of physiological characteristics (age, sex) and pathophysiological conditions (sleep apnea), relative to standard 30-s scoring. We make the model publicly available to facilitate large-scale studies with heterogeneous electrode setups and to accelerate the discovery of novel biomarkers in sleep.

